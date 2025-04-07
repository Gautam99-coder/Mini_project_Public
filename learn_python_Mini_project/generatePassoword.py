import random
import re
import string
import getpass

def generate_password(length=12, include_special=True):
    """Generate a random password with specified length and complexity"""
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation
    
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        # Ensure password meets basic complexity requirements
        if (re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password) and
            (not include_special or re.search(r'[^A-Za-z0-9]', password))):
            return password

def check_password_strength(password):
    """Evaluate password strength and provide feedback"""
    strength = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
    # Complexity checks
    checks = [
        (r'[A-Z]', "uppercase letter"),
        (r'[a-z]', "lowercase letter"),
        (r'[0-9]', "digit"),
        (r'[^A-Za-z0-9]', "special character")
    ]
    
    for pattern, description in checks:
        if re.search(pattern, password):
            strength += 1
        else:
            feedback.append(f"Missing {description}")
    
    # Strength rating
    if strength >= 6:
        rating = "Strong"
    elif strength >= 4:
        rating = "Moderate"
    else:
        rating = "Weak"
    
    return rating, feedback

def password_manager():
    print("Password Generator & Strength Checker")
    print("1. Generate Strong Password")
    print("2. Check Password Strength")
    print("3. Exit")
    
    while True:
        choice = input("\nSelect option (1-3): ")
        
        if choice == '1':
            try:
                length = int(input("Enter password length (default 12): ") or 12)
                special = input("Include special characters? (y/n): ").lower() == 'y'
                password = generate_password(length, special)
                print(f"\nGenerated Password: {password}")
                
                # Verify strength of generated password
                rating, _ = check_password_strength(password)
                print(f"Strength: {rating}")
                
                print("\nImportant: Store this password securely!")
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == '2':
            # Use getpass to hide password input
            password = getpass.getpass("Enter password to check: ")
            rating, feedback = check_password_strength(password)
            
            print(f"\nPassword Strength: {rating}")
            if feedback:
                print("\nSuggestions for improvement:")
                for item in feedback:
                    print(f"- {item}")
            else:
                print("Great job! Your password meets all basic requirements.")
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-3.")

if __name__ == "__main__":
    password_manager()
