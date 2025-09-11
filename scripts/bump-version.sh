#!/bin/bash
# Version bumping script for cmsketch

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if bump2version is installed
if ! command -v bump2version &> /dev/null; then
    print_error "bump2version is not installed!"
    print_status "Installing bump2version..."
    pip install bump2version
fi

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "Not in a git repository!"
    exit 1
fi

# Check if there are uncommitted changes
if ! git diff-index --quiet HEAD --; then
    print_warning "You have uncommitted changes!"
    print_status "Current changes:"
    git status --short
    echo ""
    read -p "Do you want to continue? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_status "Aborted."
        exit 1
    fi
fi

# Get current version
CURRENT_VERSION=$(cat VERSION 2>/dev/null || echo "unknown")
print_status "Current version: $CURRENT_VERSION"

# Show available options
echo ""
echo "Choose version bump type:"
echo "1) patch (0.1.0 → 0.1.1) - bug fixes"
echo "2) minor (0.1.0 → 0.2.0) - new features"
echo "3) major (0.1.0 → 1.0.0) - breaking changes"
echo "4) dry-run - show what would change"
echo "5) cancel"
echo ""

read -p "Enter choice (1-5): " choice

case $choice in
    1)
        BUMP_TYPE="patch"
        ;;
    2)
        BUMP_TYPE="minor"
        ;;
    3)
        BUMP_TYPE="major"
        ;;
    4)
        print_status "Running dry-run..."
        bump2version --dry-run --verbose patch
        exit 0
        ;;
    5)
        print_status "Cancelled."
        exit 0
        ;;
    *)
        print_error "Invalid choice!"
        exit 1
        ;;
esac

# Confirm the bump
echo ""
print_warning "This will bump the $BUMP_TYPE version and create a git tag."
read -p "Continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_status "Aborted."
    exit 1
fi

# Perform the bump
print_status "Bumping $BUMP_TYPE version..."
bump2version --commit --tag $BUMP_TYPE

# Get new version
NEW_VERSION=$(cat VERSION)
print_success "Version bumped: $CURRENT_VERSION → $NEW_VERSION"

# Show what changed
print_status "Changes made:"
git show --stat HEAD

echo ""
print_status "Next steps:"
echo "1. Push changes: git push origin main --tags"
echo "2. Create release on GitHub or trigger build workflow"
echo "3. Check GitHub Actions for automated builds"

print_success "Version bump complete! 🎉"
