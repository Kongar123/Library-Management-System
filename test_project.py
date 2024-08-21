import project

def test_is_valid_isbn():
    assert project.is_valid_isbn("9781234567897") == True
    assert project.is_valid_isbn("1234567890") == False

def test_add_book():
    # Resetting data
    project.books = []
    project.add_book("9781234567897", "Test Book", "Test Author", 5)
    
    assert len(project.books) == 1
    assert project.books[0]["Title"] == "Test Book"

def test_add_member():
    # Resetting data
    project.members = []
    project.add_member(1, "John Doe")
    
    assert len(project.members) == 1
    assert project.members[0]["Name"] == "John Doe"

def test_search_books():
    project.add_book("9781234567897", "Test Book", "Test Author", 5)
    
    search_result = project.search_books("Test Book")
    assert search_result[0]["ISBN"] == "9781234567897"

    search_result = project.search_books("Nonexistent Book")
    assert len(search_result) == 0

def test_issue_book():
    project.add_member(1, "John Doe")
    project.add_book("9781234567897", "Test Book", "Test Author", 5)
    
    result = project.issue_book(1, "9781234567897")
    assert result == "Book issued successfully."
    assert project.books[0]["Copies"] == 4
    assert len(project.members[0]["Borrowed Books"]) == 1

def test_return_book():
    project.add_member(1, "John Doe")
    project.add_book("9781234567897", "Test Book", "Test Author", 5)
    project.issue_book(1, "9781234567897")
    
    result = project.return_book(1, "9781234567897")
    assert result == "Book returned successfully."




