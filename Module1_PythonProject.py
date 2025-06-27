import tkinter as tk
from tkinter import messagebox
import re
import json
import os
import hashlib
from datetime import datetime

class ModernSignupApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Modern Signup Portal")
        self.root.geometry("500x700")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Initialize user data storage
        self.users_file = "users.json"
        self.load_users()
        
        # Color scheme
        self.colors = {
            'bg': '#1a1a2e',
            'card': '#16213e',
            'accent': '#0f4c75',
            'button': '#27ae60',
            'button_hover': '#2ecc71',
            'text': '#ffffff',
            'text_secondary': '#a0a0a0',
            'error': '#e74c3c',
            'success': '#27ae60'
        }
        
        self.create_ui()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"500x700+{x}+{y}")
    
    def load_users(self):
        """Load existing users from JSON file"""
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, 'r') as f:
                    self.users = json.load(f)
            else:
                self.users = {}
        except:
            self.users = {}
    
    def save_users(self):
        """Save users to JSON file"""
        try:
            with open(self.users_file, 'w') as f:
                json.dump(self.users, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save user data: {str(e)}")
    
    def hash_password(self, password):
        """Hash password for security"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def create_ui(self):
        """Create the user interface"""
        # Create main scrollable frame
        main_canvas = tk.Canvas(self.root, bg=self.colors['bg'], highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        scrollable_frame = tk.Frame(main_canvas, bg=self.colors['bg'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )
        
        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        main_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            main_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        main_canvas.bind("<MouseWheel>", _on_mousewheel)
        
        # Main container
        main_frame = tk.Frame(scrollable_frame, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True, padx=30, pady=30)
        
        # Header
        header_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        header_frame.pack(fill='x', pady=(0, 30))
        
        title = tk.Label(header_frame, text="Create Account",
                        font=('Segoe UI', 28, 'bold'),
                        fg=self.colors['text'],
                        bg=self.colors['bg'])
        title.pack()
        
        subtitle = tk.Label(header_frame, text="Join us today and get started",
                           font=('Segoe UI', 12),
                           fg=self.colors['text_secondary'],
                           bg=self.colors['bg'])
        subtitle.pack(pady=(5, 0))
        
        # Card frame
        card_frame = tk.Frame(main_frame, bg=self.colors['card'], relief='flat')
        card_frame.pack(fill='x', pady=10)
        
        # Add subtle border effect
        border_frame = tk.Frame(card_frame, bg=self.colors['accent'], height=3)
        border_frame.pack(fill='x')
        
        # Form container
        form_frame = tk.Frame(card_frame, bg=self.colors['card'])
        form_frame.pack(fill='x', padx=30, pady=30)
        
        # Username field
        self.create_input_field(form_frame, "Username", "username_entry")
        
        # Email field
        self.create_input_field(form_frame, "Email Address", "email_entry")
        
        # Password field
        self.create_input_field(form_frame, "Password", "password_entry", show="*")
        
        # Confirm Password field
        self.create_input_field(form_frame, "Confirm Password", "confirm_entry", show="*")
        
        # Password strength indicator
        self.strength_frame = tk.Frame(form_frame, bg=self.colors['card'])
        self.strength_frame.pack(fill='x', pady=(5, 15))
        
        self.strength_label = tk.Label(self.strength_frame, text="Password Strength: ",
                                      font=('Segoe UI', 9),
                                      fg=self.colors['text_secondary'],
                                      bg=self.colors['card'])
        self.strength_label.pack(side='left')
        
        self.strength_indicator = tk.Label(self.strength_frame, text="",
                                         font=('Segoe UI', 9, 'bold'),
                                         fg=self.colors['text_secondary'],
                                         bg=self.colors['card'])
        self.strength_indicator.pack(side='left', padx=(5, 0))
        
        self.strength_bar = tk.Frame(self.strength_frame, bg=self.colors['accent'], height=4, width=200)
        self.strength_bar.pack(side='left', padx=(10, 0))
        
        self.strength_fill = tk.Frame(self.strength_bar, bg=self.colors['accent'], height=4)
        self.strength_fill.pack(side='left', fill='y')
        
        # Bind password field to strength checker
        self.password_entry.bind('<KeyRelease>', self.check_password_strength)
        
        # Terms checkbox
        self.terms_var = tk.BooleanVar()
        terms_frame = tk.Frame(form_frame, bg=self.colors['card'])
        terms_frame.pack(fill='x', pady=(10, 20))
        
        terms_check = tk.Checkbutton(terms_frame, text="I agree to the Terms of Service and Privacy Policy",
                                    variable=self.terms_var,
                                    font=('Segoe UI', 10),
                                    fg=self.colors['text_secondary'],
                                    bg=self.colors['card'],
                                    selectcolor=self.colors['accent'],
                                    activebackground=self.colors['card'],
                                    activeforeground=self.colors['text'])
        terms_check.pack(anchor='w')
        
        # Button frame for proper spacing
        button_frame = tk.Frame(form_frame, bg=self.colors['card'])
        button_frame.pack(fill='x', pady=(10, 0))
        
        # Sign up button
        self.signup_btn = tk.Button(button_frame, text="CREATE ACCOUNT",
                                   font=('Segoe UI', 14, 'bold'),
                                   bg=self.colors['button'],
                                   fg=self.colors['text'],
                                   relief='flat',
                                   bd=0,
                                   padx=30,
                                   pady=15,
                                   cursor='hand2',
                                   command=self.handle_signup)
        self.signup_btn.pack(fill='x')
        
        # Button hover effects
        self.signup_btn.bind('<Enter>', lambda e: self.signup_btn.config(bg=self.colors['button_hover']))
        self.signup_btn.bind('<Leave>', lambda e: self.signup_btn.config(bg=self.colors['button']))
        
        # Clear form button
        clear_btn = tk.Button(button_frame, text="CLEAR FORM",
                             font=('Segoe UI', 12),
                             bg=self.colors['accent'],
                             fg=self.colors['text'],
                             relief='flat',
                             bd=0,
                             padx=30,
                             pady=10,
                             cursor='hand2',
                             command=self.clear_form)
        clear_btn.pack(fill='x', pady=(10, 0))
        
        # Clear button hover effects
        clear_btn.bind('<Enter>', lambda e: clear_btn.config(bg='#1e3a5f'))
        clear_btn.bind('<Leave>', lambda e: clear_btn.config(bg=self.colors['accent']))
        
        # Footer
        footer_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        footer_frame.pack(fill='x', pady=(30, 20))
        
        footer_text = tk.Label(footer_frame, text="Already have an account? Login here",
                              font=('Segoe UI', 11),
                              fg=self.colors['text_secondary'],
                              bg=self.colors['bg'],
                              cursor='hand2')
        footer_text.pack()
        footer_text.bind('<Button-1>', lambda e: messagebox.showinfo("Info", "Login feature would be implemented in a separate module"))
        
        # Add some bottom padding
        bottom_padding = tk.Frame(main_frame, bg=self.colors['bg'], height=50)
        bottom_padding.pack()
    
    def create_input_field(self, parent, label_text, attr_name, show=None):
        """Create a modern input field"""
        container = tk.Frame(parent, bg=self.colors['card'])
        container.pack(fill='x', pady=(0, 20))
        
        # Label
        label = tk.Label(container, text=label_text,
                        font=('Segoe UI', 11, 'bold'),
                        fg=self.colors['text'],
                        bg=self.colors['card'])
        label.pack(anchor='w', pady=(0, 8))
        
        # Entry field
        entry = tk.Entry(container,
                        font=('Segoe UI', 12),
                        bg=self.colors['accent'],
                        fg=self.colors['text'],
                        relief='flat',
                        bd=8,
                        show=show)
        entry.pack(fill='x', ipady=10)
        
        # Store reference to entry
        setattr(self, attr_name, entry)
        
        # Add focus effects
        entry.bind('<FocusIn>', lambda e: entry.config(bg='#1e3a5f'))
        entry.bind('<FocusOut>', lambda e: entry.config(bg=self.colors['accent']))
        
        return entry
    
    def check_password_strength(self, event=None):
        """Check and display password strength"""
        password = self.password_entry.get()
        
        if not password:
            self.strength_indicator.config(text="", fg=self.colors['text_secondary'])
            self.strength_fill.config(bg=self.colors['accent'], width=0)
            return
        
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("8+ characters")
        
        # Uppercase check
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("uppercase letter")
        
        # Lowercase check
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("lowercase letter")
        
        # Number check
        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("number")
        
        # Special character check
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            feedback.append("special character")
        
        # Update strength indicator
        strength_levels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]
        colors = ['#e74c3c', '#f39c12', '#f1c40f', '#2ecc71', '#27ae60']
        
        if score == 0:
            self.strength_indicator.config(text="Very Weak", fg='#e74c3c')
            self.strength_fill.config(bg='#e74c3c', width=20)
        else:
            level = min(score - 1, 4)
            self.strength_indicator.config(text=strength_levels[level], fg=colors[level])
            self.strength_fill.config(bg=colors[level], width=20 + (level * 35))
    
    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_username(self, username):
        """Validate username format"""
        # Username should be 3-20 characters, alphanumeric and underscores only
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return re.match(pattern, username) is not None
    
    def handle_signup(self):
        """Handle signup form submission"""
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()
        
        # Validation
        if not all([username, email, password, confirm_password]):
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if not self.terms_var.get():
            messagebox.showerror("Error", "Please agree to the Terms of Service!")
            return
        
        if not self.validate_username(username):
            messagebox.showerror("Error", "Username must be 3-20 characters long and contain only letters, numbers, and underscores!")
            return
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Please enter a valid email address!")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long!")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        # Check if username already exists
        if username.lower() in [u.lower() for u in self.users.keys()]:
            messagebox.showerror("Error", "Username already exists!")
            return
        
        # Check if email already exists
        for user_data in self.users.values():
            if user_data.get('email', '').lower() == email.lower():
                messagebox.showerror("Error", "Email already registered!")
                return
        
        # Save user
        self.users[username] = {
            'email': email,
            'password': self.hash_password(password),
            'created_at': datetime.now().isoformat(),
            'last_login': None,
            'profile_complete': False
        }
        
        self.save_users()
        
        # Success message
        messagebox.showinfo("Success", 
                           f"🎉 Account created successfully!\n\n"
                           f"Username: {username}\n"
                           f"Email: {email}\n\n"
                           f"Welcome to our platform! You can now login with your credentials.")
        
        # Clear form
        self.clear_form()
    
    def clear_form(self):
        """Clear all form fields"""
        self.username_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_entry.delete(0, tk.END)
        self.terms_var.set(False)
        self.strength_indicator.config(text="", fg=self.colors['text_secondary'])
        self.strength_fill.config(bg=self.colors['accent'], width=0)
        
        # Focus on first field
        self.username_entry.focus()
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = ModernSignupApp()
    app.run()
