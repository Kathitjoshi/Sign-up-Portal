# Modern Signup Portal

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Version](https://img.shields.io/badge/Version-1.0-orange.svg)
![Security](https://img.shields.io/badge/Security-SHA256-red.svg)

A modern, secure user registration system built with Python and Tkinter, featuring a sleek dark theme UI with real-time password strength validation and comprehensive form validation.

## 🌟 Features

### 🔐 Security Features
- **Password Hashing**: SHA-256 encryption for secure password storage
- **Input Validation**: Comprehensive form validation and sanitization
- **Email Validation**: Regex-based email format verification
- **Username Uniqueness**: Prevents duplicate usernames
- **Password Confirmation**: Double verification for password accuracy

### 🎨 User Interface
- **Modern Dark Theme**: Professional dark UI with smooth animations
- **Scrollable Interface**: Responsive design that adapts to content
- **Real-time Password Strength**: Visual indicator with color-coded feedback
- **Hover Effects**: Interactive buttons with visual feedback
- **Centered Layout**: Automatically centers window on screen
- **Form Validation**: Instant feedback on input requirements

### 📝 Registration Features
- **User Profile Creation**: Complete signup process with validation
- **Terms Agreement**: Terms of Service acceptance requirement
- **Profile Data Storage**: JSON-based user information storage
- **Clear Form Function**: Easy form reset functionality

## 📋 Requirements

- Python 3.6 or higher
- Tkinter (usually comes with Python)
- JSON support (built-in)
- Hashlib (built-in)
- Regular expressions (built-in)
- DateTime (built-in)

## 🚀 Installation

1. **Download the signup module:**
   ```bash
   # Save Module1_PythonProject.py to your desired directory
   ```

2. **Ensure Python is installed:**
   ```bash
   python --version
   ```

3. **No additional dependencies required** - uses only Python standard library

## 💻 Usage

### Running the Signup Portal
```bash
python Module1_PythonProject.py
```

### Registration Process
1. **Enter Username** (3-20 characters, alphanumeric + underscores)
2. **Enter Email Address** (valid email format required)
3. **Create Password** (minimum 6 characters, strength indicator provided)
4. **Confirm Password** (must match the original password)
5. **Accept Terms** (check the Terms of Service agreement)
6. **Click "CREATE ACCOUNT"** to complete registration


## 🔧 Configuration

### Color Scheme
```python
colors = {
    'bg': '#1a1a2e',           # Background
    'card': '#16213e',         # Card/Form background
    'accent': '#0f4c75',       # Input fields
    'button': '#27ae60',       # Primary buttons
    'button_hover': '#2ecc71',  # Button hover state
    'text': '#ffffff',         # Primary text
    'text_secondary': '#a0a0a0', # Secondary text
    'error': '#e74c3c',        # Error messages
    'success': '#27ae60'       # Success messages
}
```

### Validation Rules
- **Username**: 3-20 characters, alphanumeric + underscores only
- **Email**: Standard email format (user@domain.ext)
- **Password**: Minimum 6 characters
- **Password Strength Factors**: Length, uppercase, lowercase, numbers, special characters

## 📊 Password Strength Levels

### 🔒 Strength Indicators
- **Very Weak** (Red): Basic input, doesn't meet requirements
- **Weak** (Orange): Meets minimum length only
- **Fair** (Yellow): Length + some character variety
- **Good** (Light Green): Most requirements met
- **Strong** (Green): All requirements satisfied

### 💪 Strength Requirements
1. **Length**: 8+ characters
2. **Uppercase**: At least one uppercase letter (A-Z)
3. **Lowercase**: At least one lowercase letter (a-z)
4. **Numbers**: At least one digit (0-9)
5. **Special Characters**: At least one special character (!@#$%^&*(),.?":{}|<>)

## 💾 Data Storage

User data is stored in `users.json`:

```json
{
  "username": {
    "email": "user@example.com",
    "password": "hashed_password_string",
    "created_at": "2024-01-01T12:00:00.000000",
    "last_login": null,
    "profile_complete": false
  }
}
```

## 🎨 UI Components

### Form Fields
- **Username Input**: Real-time validation feedback
- **Email Input**: Format validation on submission
- **Password Input**: Live strength indicator
- **Confirm Password**: Match validation
- **Terms Checkbox**: Required for registration

### Interactive Elements
- **CREATE ACCOUNT Button**: Primary action with hover effects
- **CLEAR FORM Button**: Secondary action to reset form
- **Password Strength Bar**: Visual progress indicator
- **Focus Effects**: Input field highlighting on focus

## 🔐 Security Features

### ✅ Current Security Measures
- **SHA-256 Password Hashing**: Secure password storage
- **Input Sanitization**: Prevents basic injection attacks
- **Email Validation**: Regex-based format checking
- **Username Validation**: Alphanumeric + underscore restriction
- **Duplicate Prevention**: Checks for existing usernames and emails

### ⚠️ Production Considerations
For production deployment, consider:
- **Salt-based hashing** (bcrypt/scrypt instead of SHA-256)
- **Database storage** instead of JSON files
- **Rate limiting** for registration attempts
- **Email verification** before account activation
- **CAPTCHA integration** for bot prevention
- **Audit logging** for security tracking

## 🛠️ Customization

### Changing Window Size
```python
self.root.geometry("500x700")  # width x height
```

### Modifying Colors
```python
self.colors['button'] = '#your_color_here'
```

### Adjusting Validation
```python
def validate_username(self, username):
    # Modify pattern for different requirements
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    return re.match(pattern, username) is not None
```

## 🐛 Troubleshooting

### Common Issues

1. **"users.json permission denied"**
   - Ensure write permissions in the directory
   - Run as administrator if necessary

2. **Password strength not updating**
   - Check if password field has focus
   - Verify KeyRelease event binding

3. **Window appears off-screen**
   - Check display resolution settings
   - Modify center_window() function if needed

4. **Form not clearing**
   - Verify all entry widgets are properly referenced
   - Check clear_form() method implementation

## 🚀 Future Enhancements

- **Email verification system**
- **Profile picture upload**
- **Social media integration**
- **Multi-language support**
- **Advanced password policies**
- **Account recovery options**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/signup-enhancement`)
3. Commit your changes (`git commit -am 'Add new signup feature'`)
4. Push to the branch (`git push origin feature/signup-enhancement`)
5. Create a Pull Request


## 👨‍💻 Author

Modern Signup Portal - Secure user registration made simple.

## 🙏 Acknowledgments

- Python Tkinter documentation
- Modern UI/UX design principles
- Security best practices for user registration

---

**⭐ If you find this signup portal helpful, please consider giving it a star!**
