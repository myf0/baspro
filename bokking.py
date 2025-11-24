import tkinter as tk
from tkinter import messagebox, ttk
import json
from datetime import datetime, timedelta
import os
import random

class CampusFacilitySystem:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Campus Facility Management System")
        self.window.geometry("1200x700")
        self.window.configure(bg='#f0f2f5')
        
        # Center window on screen
        self.window.eval('tk::PlaceWindow . center')
        
        # Get current directory
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Initialize data
        self.load_data()
        self.current_user = None
        self.current_facility_type = None
        
        print("🚀 System initialized successfully")
        self.show_login_page()

    def load_data(self):
        """Load data from JSON file or create default data"""
        try:
            if os.path.exists('campus_data.json'):
                with open('campus_data.json', 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
                print("✅ Data loaded from file")
            else:
                self.create_default_data()
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            self.create_default_data()

    def create_default_data(self):
        """Create default data structure"""
        self.data = {
            "users": [
                {"username": "admin", "password": "admin123", "role": "admin", "full_name": "Administrator"},
                {"username": "dosen", "password": "dosen123", "role": "lecturer", "full_name": "Dr. Ahmad"},
                {"username": "mahasiswa", "password": "mhs123", "role": "student", "full_name": "Budi Santoso"}
            ],
            "academic_facilities": {
                "classrooms": [
                    {
                        "id": 1, "name": "C9-101", "status": "available", "current_usage": None, 
                        "capacity": 40, "facilities": ["AC", "Projector"], "color": "green", 
                        "last_updated": datetime.now().isoformat(), "blocked": False,
                        "official_schedule": [
                            {"day": "Senin", "time": "08:00-10:00", "subject": "Kalkulus", "lecturer": "Prof. Ahmad"},
                            {"day": "Selasa", "time": "10:00-12:00", "subject": "Fisika", "lecturer": "Dr. Sari"},
                            {"day": "Rabu", "time": "13:00-15:00", "subject": "Kimia", "lecturer": "Dr. Budi"}
                        ]
                    },
                    {
                        "id": 2, "name": "C9-102", "status": "occupied", "current_usage": "Kalkulus - Prof. Ahmad", 
                        "capacity": 35, "facilities": ["AC", "Whiteboard"], "color": "red", 
                        "last_updated": datetime.now().isoformat(), "blocked": False,
                        "official_schedule": [
                            {"day": "Senin", "time": "10:00-12:00", "subject": "Aljabar Linear", "lecturer": "Dr. Rina"},
                            {"day": "Kamis", "time": "08:00-10:00", "subject": "Statistika", "lecturer": "Prof. David"}
                        ]
                    },
                    {
                        "id": 3, "name": "C9-201", "status": "available", "current_usage": None,
                        "capacity": 50, "facilities": ["AC", "Projector", "Sound System"], "color": "green", 
                        "last_updated": datetime.now().isoformat(), "blocked": False,
                        "official_schedule": []
                    },
                    {
                        "id": 4, "name": "C9-202", "status": "occupied", "current_usage": "Aljabar Linear - Dr. Sari",
                        "capacity": 45, "facilities": ["AC", "Whiteboard"], "color": "red", 
                        "last_updated": datetime.now().isoformat(), "blocked": False,
                        "official_schedule": [
                            {"day": "Jumat", "time": "09:00-11:00", "subject": "Pemrograman", "lecturer": "Dr. Andi"}
                        ]
                    }
                ]
            },
            "sports_facilities": {
                "swimming_pool": [
                    {"id": 1, "name": "Kolam Renang Reguler", "status": "available", "price": 15000, 
                     "current_booking": None, "capacity": 50, "color": "green", "schedule": [], "blocked": False}
                ],
                "gym": [
                    {"id": 1, "name": "Gym Center", "status": "available", "price": 20000, 
                     "current_booking": None, "capacity": 30, "color": "green", "schedule": [], "blocked": False}
                ],
                "court": [
                    {"id": 1, "name": "Lapangan Futsal", "status": "available", "price": 50000, 
                     "current_booking": None, "capacity": 20, "color": "green", "schedule": [], "blocked": False},
                    {"id": 2, "name": "Lapangan Bulu Tangkis", "status": "available", "price": 25000, 
                     "current_booking": None, "capacity": 8, "color": "green", "schedule": [], "blocked": False},
                    {"id": 3, "name": "Lapangan Basket", "status": "occupied", "price": 40000, 
                     "current_booking": "Tim Basket UNESA", "capacity": 24, "color": "red", "schedule": [], "blocked": False}
                ]
            },
            "bookings": [],
            "transactions": [],
            "status_history": [],
            "login_history": [],
            "admin_logs": [],
            "payment_methods": ["QRIS", "Transfer Bank", "Cash", "E-Wallet"]
        }
        self.save_data()
        print("✅ Default data created")

    def save_data(self):
        """Save data to JSON file"""
        try:
            with open('campus_data.json', 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=4, default=str)
        except Exception as e:
            print(f"❌ Error saving data: {e}")

    def show_login_page(self):
        """Show login page"""
        print("🔐 Loading login page...")
        
        # Clear window
        for widget in self.window.winfo_children():
            widget.destroy()

        # Main container
        main_frame = tk.Frame(self.window, bg='#2c3e50')
        main_frame.pack(fill='both', expand=True)

        # Left side - Branding
        left_frame = tk.Frame(main_frame, bg='#34495e', width=400)
        left_frame.pack(side='left', fill='y')
        left_frame.pack_propagate(False)

        # Logo Area
        logo_frame = tk.Frame(left_frame, bg='#34495e')
        logo_frame.pack(expand=True)

        # Logo using emoji
        logo_label = tk.Label(logo_frame, text="🏛️", font=("Arial", 60), 
                             bg='#34495e', fg='white')
        logo_label.pack(pady=(150, 20))
        
        tk.Label(logo_frame, text="CAMPUS FACILITY", font=("Arial", 20, "bold"), 
                bg='#34495e', fg='white').pack()
        tk.Label(logo_frame, text="Management System", font=("Arial", 14), 
                bg='#34495e', fg='#bdc3c7').pack(pady=10)

        # Right side - Login Form
        right_frame = tk.Frame(main_frame, bg='white')
        right_frame.pack(side='right', fill='both', expand=True, padx=80)

        # Login Form
        form_frame = tk.Frame(right_frame, bg='white')
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(form_frame, text="LOGIN", font=("Arial", 24, "bold"), 
                bg='white', fg='#2c3e50').pack(pady=(0, 40))

        # Username
        tk.Label(form_frame, text="Username", font=("Arial", 11, "bold"), 
                bg='white', fg='#7f8c8d').pack(anchor='w', pady=(10, 5))
        
        self.username_entry = tk.Entry(form_frame, width=30, font=("Arial", 12), 
                                     bg='#ecf0f1', relief='solid', bd=1)
        self.username_entry.pack(pady=(0, 20), ipady=8)

        # Password
        tk.Label(form_frame, text="Password", font=("Arial", 11, "bold"), 
                bg='white', fg='#7f8c8d').pack(anchor='w', pady=(10, 5))
        
        self.password_entry = tk.Entry(form_frame, width=30, font=("Arial", 12), 
                                     show="•", bg='#ecf0f1', relief='solid', bd=1)
        self.password_entry.pack(pady=(0, 20), ipady=8)

        # Options frame
        options_frame = tk.Frame(form_frame, bg='white')
        options_frame.pack(fill='x', pady=10)

        # Remember me
        self.remember_var = tk.BooleanVar()
        remember_cb = tk.Checkbutton(options_frame, text="Remember me", 
                                    variable=self.remember_var,
                                    font=("Arial", 10), bg='white', fg='#7f8c8d')
        remember_cb.pack(side='left')

        # Register button
        register_btn = tk.Button(options_frame, text="Register", 
                                command=self.show_register_page,
                                font=("Arial", 10), bg='white', fg='#3498db', 
                                bd=0, cursor='hand2')
        register_btn.pack(side='right')

        # Login Button - FIXED: Direct command
        login_btn = tk.Button(form_frame, text="LOGIN", 
                             font=("Arial", 12, "bold"), 
                             bg='#3498db', fg='white',
                             relief='raised', bd=2,
                             command=self.handle_login,
                             width=20, height=2,
                             cursor='hand2')
        login_btn.pack(pady=20)

        # Bind Enter key
        def on_enter_key(event):
            self.handle_login()
        
        self.window.bind('<Return>', on_enter_key)
        self.username_entry.bind('<Return>', on_enter_key)
        self.password_entry.bind('<Return>', on_enter_key)

        # Focus on username
        self.username_entry.focus()
        
        print("✅ Login page ready")
        print("💡 Test credentials: admin/admin123, dosen/dosen123, mahasiswa/mhs123")

    def handle_login(self):
        """Handle login process"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        print(f"🔐 Login attempt: {username}")
        
        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields!")
            self.username_entry.focus()
            return
        
        # Check credentials
        user_found = False
        for user in self.data['users']:
            if user['username'] == username and user['password'] == password:
                self.current_user = user
                user_found = True
                
                # Log login
                login_log = {
                    'username': username,
                    'role': user['role'],
                    'timestamp': datetime.now().isoformat(),
                    'ip_address': 'localhost'
                }
                self.data['login_history'].append(login_log)
                self.save_data()
                
                print(f"✅ Login successful: {user['full_name']}")
                messagebox.showinfo("Success", f"Welcome, {user['full_name']}!")
                self.show_facility_selection()
                return
        
        if not user_found:
            print("❌ Login failed")
            messagebox.showerror("Error", "Invalid username or password!")
            self.password_entry.delete(0, tk.END)
            self.username_entry.focus()

    def show_register_page(self):
        """Show registration page"""
        register_window = tk.Toplevel(self.window)
        register_window.title("Register New Account")
        register_window.geometry("400x500")
        register_window.configure(bg='white')
        register_window.transient(self.window)
        register_window.grab_set()
        
        # Center the window
        register_window.eval('tk::PlaceWindow . center')

        tk.Label(register_window, text="REGISTER", font=("Arial", 20, "bold"), bg='white').pack(pady=20)

        # Form fields
        fields = [
            ("Full Name", "text"),
            ("Username", "text"),
            ("Password", "password"),
            ("Confirm Password", "password"),
            ("Role", "role")
        ]
        
        entries = {}
        for field, field_type in fields:
            frame = tk.Frame(register_window, bg='white')
            frame.pack(fill='x', padx=30, pady=8)
            
            tk.Label(frame, text=field, font=("Arial", 11), bg='white').pack(anchor='w')
            
            if field_type == 'role':
                role_var = tk.StringVar(value="student")
                role_frame = tk.Frame(frame, bg='white')
                role_frame.pack(fill='x', pady=5)
                
                tk.Radiobutton(role_frame, text="Mahasiswa", variable=role_var, 
                              value="student", font=("Arial", 10), bg='white').pack(side='left')
                tk.Radiobutton(role_frame, text="Dosen", variable=role_var, 
                              value="lecturer", font=("Arial", 10), bg='white').pack(side='left')
                entries[field] = role_var
            elif field_type == 'password':
                entry = tk.Entry(frame, show="•", width=30, font=("Arial", 11), relief='solid', bd=1)
                entry.pack(fill='x', pady=5)
                entries[field] = entry
            else:
                entry = tk.Entry(frame, width=30, font=("Arial", 11), relief='solid', bd=1)
                entry.pack(fill='x', pady=5)
                entries[field] = entry
        
        def submit_registration():
            # Validation
            if not all(entry.get() if hasattr(entry, 'get') else entry.get() 
                      for field, entry in entries.items() if field != "Confirm Password"):
                messagebox.showerror("Error", "Please fill all fields!")
                return
            
            if entries['Password'].get() != entries['Confirm Password'].get():
                messagebox.showerror("Error", "Passwords do not match!")
                return
            
            username = entries['Username'].get()
            # Check if username exists
            if any(user['username'] == username for user in self.data['users']):
                messagebox.showerror("Error", "Username already exists!")
                return
            
            # Add new user
            new_user = {
                "username": username,
                "password": entries['Password'].get(),
                "role": entries['Role'].get(),
                "full_name": entries['Full Name'].get()
            }
            self.data['users'].append(new_user)
            self.save_data()
            
            messagebox.showinfo("Success", "Registration successful! You can now login.")
            register_window.destroy()
        
        tk.Button(register_window, text="Register", command=submit_registration,
                 bg='#27ae60', fg='white', font=("Arial", 12), relief='raised', bd=2).pack(pady=20)

    def create_header(self, title, bg_color='#2c3e50', show_back_button=True):
        """Create header for pages"""
        header_frame = tk.Frame(self.window, bg=bg_color, height=80)
        header_frame.pack(fill='x', padx=20, pady=10)
        header_frame.pack_propagate(False)
        
        # Left section
        left_section = tk.Frame(header_frame, bg=bg_color)
        left_section.pack(side='left', padx=10)
        
        # Logo
        logo_circle = tk.Frame(left_section, bg='#3498db', width=30, height=30)
        logo_circle.pack_propagate(False)
        logo_circle.pack(side='left', padx=(0, 10))
        logo_label = tk.Label(logo_circle, text="🏛️", font=("Arial", 12), bg='#3498db', fg='white')
        logo_label.pack(expand=True)
        
        # Back button
        if show_back_button:
            back_btn = tk.Button(left_section, text="← Kembali", 
                               command=self.show_facility_selection,
                               bg='#34495e', fg='white', font=("Arial", 10))
            back_btn.pack(side='left', padx=5)
        
        # Title
        title_label = tk.Label(header_frame, text=title, 
                              font=("Arial", 16, "bold"), bg=bg_color, fg='white')
        title_label.pack(side='left', expand=True, padx=20, pady=20)
        
        # Right section - User info
        right_section = tk.Frame(header_frame, bg=bg_color)
        right_section.pack(side='right', padx=10)
        
        if self.current_user:
            user_label = tk.Label(right_section, 
                                 text=f"{self.current_user['full_name']} ({self.current_user['role']})", 
                                 font=("Arial", 11), bg=bg_color, fg='white')
            user_label.pack(side='left', padx=10)
            
            # Admin button
            if self.current_user['role'] == 'admin':
                admin_btn = tk.Button(right_section, text="Admin Dashboard", 
                                    command=self.show_admin_dashboard,
                                    bg='#9b59b6', fg='white', font=("Arial", 10))
                admin_btn.pack(side='left', padx=5)
            
            logout_btn = tk.Button(right_section, text="Logout", 
                                 command=self.logout,
                                 bg='#e74c3c', fg='white', font=("Arial", 10))
            logout_btn.pack(side='left', padx=5)
        
        return header_frame

    def show_facility_selection(self):
        """Show facility selection page"""
        print("🏢 Loading facility selection...")
        
        # Clear window
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Header
        self.create_header("PILIH JENIS FASILITAS", '#2c3e50', show_back_button=False)
        
        # Main content
        main_frame = tk.Frame(self.window, bg='#f0f2f5')
        main_frame.pack(fill='both', expand=True, padx=50, pady=50)
        
        tk.Label(main_frame, text="PILIH JENIS FASILITAS", 
                font=("Arial", 18, "bold"), bg='#f0f2f5').pack(pady=20)
        
        # Cards container
        cards_container = tk.Frame(main_frame, bg='#f0f2f5')
        cards_container.pack(expand=True, pady=40)
        
        # Academic Card
        academic_frame = tk.Frame(cards_container, bg='#f0f2f5')
        academic_frame.pack(side='left', padx=30)
        
        academic_card = tk.Frame(academic_frame, bg='white', relief='raised', bd=2, 
                               width=300, height=200, cursor='hand2')
        academic_card.pack()
        academic_card.pack_propagate(False)
        academic_card.bind("<Button-1>", lambda e: self.select_facility_type('academic'))
        
        tk.Label(academic_card, text="🎓", font=("Arial", 40), bg='white').pack(pady=20)
        tk.Label(academic_card, text="FASILITAS PERKULIAHAN", 
                font=("Arial", 14, "bold"), bg='white').pack()
        tk.Label(academic_card, text="Manajemen Ruang Kelas", 
                font=("Arial", 11), bg='white', fg='#7f8c8d').pack(pady=10)
        
        # Sports Card
        sports_frame = tk.Frame(cards_container, bg='#f0f2f5')
        sports_frame.pack(side='right', padx=30)
        
        sports_card = tk.Frame(sports_frame, bg='white', relief='raised', bd=2, 
                             width=300, height=200, cursor='hand2')
        sports_card.pack()
        sports_card.pack_propagate(False)
        sports_card.bind("<Button-1>", lambda e: self.select_facility_type('sports'))
        
        tk.Label(sports_card, text="⚽", font=("Arial", 40), bg='white').pack(pady=20)
        tk.Label(sports_card, text="FASILITAS OLAHRAGA", 
                font=("Arial", 14, "bold"), bg='white').pack()
        tk.Label(sports_card, text="Booking Lapangan & Tiket", 
                font=("Arial", 11), bg='white', fg='#7f8c8d').pack(pady=10)
        
        # Hover effects
        for card in [academic_card, sports_card]:
            card.bind("<Enter>", lambda e, c=card: c.config(bg='#ecf0f1'))
            card.bind("<Leave>", lambda e, c=card: c.config(bg='white'))
        
        print("✅ Facility selection ready")

    def select_facility_type(self, facility_type):
        """Select facility type"""
        self.current_facility_type = facility_type
        print(f"🎯 Selected: {facility_type}")
        
        if facility_type == 'academic':
            self.show_academic_dashboard()
        else:
            self.show_sports_dashboard()

    def show_academic_dashboard(self):
        """Show academic facilities dashboard"""
        print("📚 Loading academic dashboard...")
        
        # Clear window
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Header
        self.create_header("CLASS TRACK - MANAJEMEN RUANG KELAS", '#2c3e50')
        
        # Main content
        main_frame = tk.Frame(self.window, bg='#f0f2f5')
        main_frame.pack(fill='both', expand=True, padx=40, pady=20)
        
        # Title
        tk.Label(main_frame, text="STATUS RUANGAN KELAS - GEDUNG C9", 
                font=("Arial", 16, "bold"), bg='#f0f2f5').pack(pady=10)
        
        # Legend
        legend_frame = tk.Frame(main_frame, bg='#f0f2f5')
        legend_frame.pack(pady=10)
        
        tk.Label(legend_frame, text="● TERSEDIA", fg='green', 
                font=("Arial", 10, "bold"), bg='#f0f2f5').pack(side='left', padx=10)
        tk.Label(legend_frame, text="● DIPAKAI", fg='red', 
                font=("Arial", 10, "bold"), bg='#f0f2f5').pack(side='left', padx=10)
        tk.Label(legend_frame, text="● BLOKIR", fg='gray', 
                font=("Arial", 10, "bold"), bg='#f0f2f5').pack(side='left', padx=10)
        
        # Classroom grid
        grid_frame = tk.Frame(main_frame, bg='#f0f2f5')
        grid_frame.pack(fill='both', expand=True, pady=20)
        
        # Create classroom cards
        classrooms = self.data['academic_facilities']['classrooms']
        for i, room in enumerate(classrooms):
            row = i // 2
            col = i % 2
            
            # Determine color based on status
            if room.get('blocked', False):
                color = 'gray'
                status = "BLOKIR"
            elif room['status'] == 'available':
                color = 'green'
                status = "TERSEDIA"
            else:
                color = 'red'
                status = "DIPAKAI"
            
            # Create card
            card = tk.Frame(grid_frame, bg='white', relief='raised', bd=2, 
                          width=300, height=150)
            card.grid(row=row, column=col, padx=20, pady=20, sticky='nsew')
            card.grid_propagate(False)
            
            # Header
            header = tk.Frame(card, bg=color, height=35)
            header.pack(fill='x')
            header.pack_propagate(False)
            
            tk.Label(header, text=room['name'], font=("Arial", 12, "bold"), 
                    bg=color, fg='white').pack(pady=8)
            
            # Info
            info_frame = tk.Frame(card, bg='white')
            info_frame.pack(expand=True, fill='both', padx=15, pady=10)
            
            # Status
            tk.Label(info_frame, text=status, font=("Arial", 11, "bold"), 
                    fg=color).pack(anchor='w', pady=2)
            
            # Schedule density
            density = self.calculate_schedule_density(room)
            density_color = 'red' if density == 'Padat' else 'orange' if density == 'Sedang' else 'green'
            tk.Label(info_frame, text=f"Kepadatan: {density}", 
                    font=("Arial", 9, "bold"), fg=density_color).pack(anchor='w', pady=2)
            
            # Current usage
            if room['current_usage']:
                tk.Label(info_frame, text=room['current_usage'], 
                        font=("Arial", 9), wraplength=250, justify='left').pack(anchor='w', pady=2)
            
            # Facilities
            facilities = "Fasilitas: " + ", ".join(room['facilities'])
            tk.Label(info_frame, text=facilities, 
                    font=("Arial", 8), fg='gray').pack(anchor='w', pady=2)
            
            # Click handler
            card.bind("<Button-1>", lambda e, r=room: self.show_classroom_detail(r))
            for child in card.winfo_children():
                child.bind("<Button-1>", lambda e, r=room: self.show_classroom_detail(r))
        
        # Configure grid
        grid_frame.grid_rowconfigure(0, weight=1)
        grid_frame.grid_rowconfigure(1, weight=1)
        grid_frame.grid_columnconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(1, weight=1)
        
        print("✅ Academic dashboard ready")

    def calculate_schedule_density(self, classroom):
        """Calculate schedule density"""
        schedule_count = len(classroom.get('official_schedule', []))
        
        if schedule_count >= 5:
            return "Padat"
        elif schedule_count >= 3:
            return "Sedang"
        else:
            return "Senggang"

    def show_classroom_detail(self, classroom):
        """Show classroom details"""
        detail_window = tk.Toplevel(self.window)
        detail_window.title(f"Detail {classroom['name']}")
        detail_window.geometry("500x600")
        detail_window.configure(bg='white')
        detail_window.transient(self.window)
        
        # Center window
        detail_window.eval('tk::PlaceWindow . center')
        
        # Header
        header_color = 'gray' if classroom.get('blocked', False) else classroom['color']
        header_frame = tk.Frame(detail_window, bg=header_color, height=60)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text=classroom['name'], 
                font=("Arial", 18, "bold"), bg=header_color, fg='white').pack(pady=15)
        
        # Content
        content_frame = tk.Frame(detail_window, bg='white')
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Basic info
        status_text = "BLOKIR" if classroom.get('blocked', False) else "TERSEDIA" if classroom['status'] == 'available' else "DIPAKAI"
        tk.Label(content_frame, text=f"Status: {status_text}", 
                font=("Arial", 14, "bold"), bg='white', fg=header_color).pack(anchor='w', pady=10)
        
        tk.Label(content_frame, text=f"Kapasitas: {classroom['capacity']} orang", 
                font=("Arial", 11), bg='white').pack(anchor='w', pady=5)
        
        facilities = "Fasilitas: " + ", ".join(classroom['facilities'])
        tk.Label(content_frame, text=facilities, 
                font=("Arial", 11), bg='white').pack(anchor='w', pady=5)
        
        if classroom['current_usage']:
            tk.Label(content_frame, text=f"Penggunaan: {classroom['current_usage']}", 
                    font=("Arial", 11), bg='white').pack(anchor='w', pady=5)
        
        # Official schedule
        tk.Label(content_frame, text="Jadwal Resmi:", 
                font=("Arial", 12, "bold"), bg='white').pack(anchor='w', pady=(15, 5))
        
        schedule_frame = tk.Frame(content_frame, bg='white')
        schedule_frame.pack(fill='x', pady=5)
        
        schedules = classroom.get('official_schedule', [])
        if schedules:
            for schedule in schedules:
                text = f"• {schedule['day']} {schedule['time']} - {schedule['subject']} ({schedule['lecturer']})"
                tk.Label(schedule_frame, text=text, font=("Arial", 10), 
                        bg='white', justify='left').pack(anchor='w')
        else:
            tk.Label(schedule_frame, text="Tidak ada jadwal resmi", 
                    font=("Arial", 10), bg='white', fg='gray').pack(anchor='w')
        
        # Action buttons
        action_frame = tk.Frame(detail_window, bg='white')
        action_frame.pack(fill='x', padx=20, pady=10)
        
        if not classroom.get('blocked', False):
            if classroom['status'] == 'available':
                book_btn = tk.Button(action_frame, text="📅 Booking Kelas", 
                                   command=lambda: self.show_classroom_booking_form(classroom),
                                   bg='#27ae60', fg='white', font=("Arial", 11))
                book_btn.pack(side='left', padx=5)
            else:
                if self.current_user and self.current_user['role'] in ['lecturer', 'admin']:
                    change_btn = tk.Button(action_frame, text="✏️ Ubah Status", 
                                         command=lambda: self.show_status_change_form(classroom),
                                         bg='#e74c3c', fg='white', font=("Arial", 11))
                    change_btn.pack(side='left', padx=5)
        
        # Edit schedule (dosen/admin only)
        if self.current_user and self.current_user['role'] in ['lecturer', 'admin']:
            schedule_btn = tk.Button(action_frame, text="📝 Edit Jadwal", 
                                   command=lambda: self.show_schedule_editor(classroom),
                                   bg='#3498db', fg='white', font=("Arial", 11))
            schedule_btn.pack(side='left', padx=5)
        
        # Close button
        close_btn = tk.Button(action_frame, text="Kembali", 
                            command=detail_window.destroy,
                            bg='#95a5a6', fg='white', font=("Arial", 11))
        close_btn.pack(side='right', padx=5)

    def show_classroom_booking_form(self, classroom):
        """Show classroom booking form"""
        booking_window = tk.Toplevel(self.window)
        booking_window.title(f"Booking {classroom['name']}")
        booking_window.geometry("500x600")
        booking_window.configure(bg='white')
        booking_window.transient(self.window)
        booking_window.eval('tk::PlaceWindow . center')
        
        tk.Label(booking_window, text=f"BOOKING KELAS - {classroom['name']}", 
                font=("Arial", 16, "bold")).pack(pady=20)
        
        # Official schedule
        schedule_frame = tk.LabelFrame(booking_window, text="Jadwal Resmi Kelas", 
                                     font=("Arial", 12, "bold"))
        schedule_frame.pack(fill='x', padx=30, pady=10)
        
        official_schedule = classroom.get('official_schedule', [])
        if official_schedule:
            for schedule in official_schedule:
                schedule_text = f"• {schedule['day']} {schedule['time']} - {schedule['subject']}"
                tk.Label(schedule_frame, text=schedule_text, font=("Arial", 10), 
                        justify='left').pack(anchor='w', padx=10, pady=2)
        else:
            tk.Label(schedule_frame, text="Tidak ada jadwal resmi", 
                    font=("Arial", 10), fg='gray').pack(pady=5)
        
        # Form fields
        fields = [
            ("Nama Pemesan", "text"),
            ("NIM / ID", "text"), 
            ("Mata Kuliah", "text"),
            ("Kelas", "text"),
            ("Dosen Pengampu", "text"),
            ("Hari", "combo", ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]),
            ("Waktu Mulai", "text"),
            ("Waktu Selesai", "text"),
            ("Tanggal", "text")
        ]
        
        entries = {}
        for field, field_type, *options in fields:
            frame = tk.Frame(booking_window)
            frame.pack(fill='x', padx=30, pady=5)
            
            tk.Label(frame, text=field, font=("Arial", 10)).pack(anchor='w')
            
            if field_type == 'combo':
                entry = ttk.Combobox(frame, values=options[0], width=27, font=("Arial", 10))
            elif field_type == 'number':
                entry = tk.Spinbox(frame, from_=1, to=8, width=30, font=("Arial", 10))
            else:
                entry = tk.Entry(frame, width=30, font=("Arial", 10), relief='solid', bd=1)
            
            entry.pack(fill='x', pady=2)
            entries[field] = entry
        
        def submit_booking():
            # Process booking
            booking_data = {
                'facility_type': 'academic',
                'classroom': classroom['name'],
                'timestamp': datetime.now().isoformat(),
                'status': 'pending_payment'
            }
            
            for field, entry in entries.items():
                booking_data[field.lower().replace(' ', '_')] = entry.get() if hasattr(entry, 'get') else entry
            
            self.data['bookings'].append(booking_data)
            
            # Update classroom status
            classroom['status'] = 'occupied'
            classroom['color'] = 'red'
            classroom['current_usage'] = f"{entries['Mata Kuliah'].get()} - {entries['Dosen Pengampu'].get()}"
            classroom['last_updated'] = datetime.now().isoformat()
            
            self.save_data()
            
            # Show receipt
            self.show_booking_receipt(booking_data, "Kelas")
            booking_window.destroy()
            self.show_academic_dashboard()
        
        tk.Button(booking_window, text="📋 Konfirmasi Booking", command=submit_booking, 
                 bg='#27ae60', fg='white', font=("Arial", 12), relief='raised', bd=2).pack(pady=20)

    def show_schedule_editor(self, classroom):
        """Show schedule editor"""
        editor_window = tk.Toplevel(self.window)
        editor_window.title(f"Edit Jadwal {classroom['name']}")
        editor_window.geometry("500x500")
        editor_window.configure(bg='white')
        editor_window.transient(self.window)
        editor_window.eval('tk::PlaceWindow . center')
        
        tk.Label(editor_window, text=f"EDIT JADWAL - {classroom['name']}", 
                font=("Arial", 16, "bold")).pack(pady=20)
        
        # Current schedule
        current_frame = tk.LabelFrame(editor_window, text="Jadwal Saat Ini", 
                                    font=("Arial", 12, "bold"))
        current_frame.pack(fill='x', padx=30, pady=10)
        
        official_schedule = classroom.get('official_schedule', [])
        schedule_vars = []
        
        if official_schedule:
            for i, schedule in enumerate(official_schedule):
                frame = tk.Frame(current_frame, bg='white')
                frame.pack(fill='x', padx=10, pady=2)
                
                var = tk.BooleanVar()
                chk = tk.Checkbutton(frame, variable=var, bg='white')
                chk.pack(side='left')
                schedule_vars.append((var, i))
                
                schedule_text = f"{schedule['day']} {schedule['time']} - {schedule['subject']} ({schedule['lecturer']})"
                tk.Label(frame, text=schedule_text, font=("Arial", 10), bg='white').pack(side='left')
        else:
            tk.Label(current_frame, text="Tidak ada jadwal", 
                    font=("Arial", 10), fg='gray', bg='white').pack(pady=5)
        
        # Add new schedule
        new_frame = tk.LabelFrame(editor_window, text="Tambah Jadwal Baru", 
                                font=("Arial", 12, "bold"))
        new_frame.pack(fill='x', padx=30, pady=10)
        
        new_entries = {}
        new_fields = [
            ("Hari", "combo", ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]),
            ("Waktu (contoh: 08:00-10:00)", "text"),
            ("Mata Kuliah", "text"),
            ("Dosen", "text")
        ]
        
        for field, field_type, *options in new_fields:
            frame = tk.Frame(new_frame, bg='white')
            frame.pack(fill='x', padx=10, pady=5)
            
            tk.Label(frame, text=field, font=("Arial", 10), bg='white').pack(anchor='w')
            
            if field_type == 'combo':
                entry = ttk.Combobox(frame, values=options[0], width=20, font=("Arial", 10))
            else:
                entry = tk.Entry(frame, width=25, font=("Arial", 10), relief='solid', bd=1)
            
            entry.pack(fill='x', pady=2)
            new_entries[field] = entry
        
        def save_schedule():
            # Remove selected schedules
            for var, index in schedule_vars:
                if var.get():
                    classroom['official_schedule'].pop(index)
            
            # Add new schedule
            if all(entry.get() for entry in new_entries.values()):
                new_schedule = {
                    'day': new_entries['Hari'].get(),
                    'time': new_entries['Waktu (contoh: 08:00-10:00)'].get(),
                    'subject': new_entries['Mata Kuliah'].get(),
                    'lecturer': new_entries['Dosen'].get()
                }
                classroom['official_schedule'].append(new_schedule)
            
            self.save_data()
            messagebox.showinfo("Success", "Jadwal berhasil diupdate!")
            editor_window.destroy()
        
        tk.Button(editor_window, text="💾 Simpan Perubahan", command=save_schedule,
                 bg='#3498db', fg='white', font=("Arial", 12), relief='raised', bd=2).pack(pady=20)

    def show_status_change_form(self, classroom):
        """Show status change form"""
        status_window = tk.Toplevel(self.window)
        status_window.title(f"Ubah Status {classroom['name']}")
        status_window.geometry("400x400")
        status_window.configure(bg='white')
        status_window.transient(self.window)
        status_window.eval('tk::PlaceWindow . center')
        
        tk.Label(status_window, text=f"UBAH STATUS - {classroom['name']}", 
                font=("Arial", 16, "bold")).pack(pady=20)
        
        # Status options
        tk.Label(status_window, text="Pilih Status Baru:", font=("Arial", 12)).pack(pady=10)
        
        status_var = tk.StringVar(value="available")
        
        tk.Radiobutton(status_window, text="Kelas Selesai (Tersedia)", 
                      variable=status_var, value="available", font=("Arial", 11), bg='white').pack(anchor='w', padx=50, pady=5)
        tk.Radiobutton(status_window, text="Libur (Tersedia)", 
                      variable=status_var, value="available", font=("Arial", 11), bg='white').pack(anchor='w', padx=50, pady=5)
        
        # Reason field
        tk.Label(status_window, text="Alasan Perubahan:", font=("Arial", 12)).pack(pady=10)
        reason_entry = tk.Entry(status_window, width=40, font=("Arial", 11), relief='solid', bd=1)
        reason_entry.pack(pady=5)
        
        def submit_status_change():
            new_status = status_var.get()
            reason = reason_entry.get()
            
            # Update classroom
            classroom['status'] = new_status
            classroom['color'] = 'green' if new_status == 'available' else 'red'
            classroom['current_usage'] = None if new_status == 'available' else classroom['current_usage']
            classroom['last_updated'] = datetime.now().isoformat()
            
            # Add to history
            history_entry = {
                'classroom': classroom['name'],
                'old_status': 'occupied',
                'new_status': new_status,
                'changed_by': self.current_user['username'],
                'reason': reason,
                'timestamp': datetime.now().isoformat()
            }
            self.data['status_history'].append(history_entry)
            
            self.save_data()
            
            messagebox.showinfo("Success", f"Status {classroom['name']} berhasil diubah!")
            status_window.destroy()
            self.show_academic_dashboard()
        
        tk.Button(status_window, text="💾 Simpan Perubahan", command=submit_status_change,
                 bg='#3498db', fg='white', font=("Arial", 12), relief='raised', bd=2).pack(pady=20)

    def show_sports_dashboard(self):
        """Show sports facilities dashboard"""
        print("⚽ Loading sports dashboard...")
        
        # Clear window
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Header
        self.create_header("SPORTS FACILITY - BOOKING & TIKET", '#27ae60')
        
        # Main content
        main_frame = tk.Frame(self.window, bg='#f0f2f5')
        main_frame.pack(fill='both', expand=True, padx=40, pady=20)
        
        # Categories
        categories = [
            {"name": "🏊 KOLAM RENANG", "data": self.data['sports_facilities']['swimming_pool'], "color": "#3498db"},
            {"name": "💪 GYM CENTER", "data": self.data['sports_facilities']['gym'], "color": "#e74c3c"},
            {"name": "⚽ LAPANGAN", "data": self.data['sports_facilities']['court'], "color": "#f39c12"}
        ]
        
        for category in categories:
            category_frame = tk.LabelFrame(main_frame, text=category['name'], 
                                         font=("Arial", 14, "bold"), bg='white', fg=category['color'])
            category_frame.pack(fill='x', pady=15, padx=20)
            
            for facility in category['data']:
                facility_frame = tk.Frame(category_frame, bg='white')
                facility_frame.pack(fill='x', padx=10, pady=8)
                
                status_color = 'gray' if facility.get('blocked', False) else facility['color']
                status_text = "BLOKIR" if facility.get('blocked', False) else "TERSEDIA" if facility['status'] == 'available' else "TERBOOKING"
                
                # Facility info
                info_text = f"{facility['name']} - Rp {facility['price']:,} - Kapasitas: {facility['capacity']} orang"
                tk.Label(facility_frame, text=info_text, font=("Arial", 11), bg='white').pack(side='left')
                
                # Status
                tk.Label(facility_frame, text=status_text, font=("Arial", 10, "bold"), 
                        fg=status_color).pack(side='left', padx=20)
                
                # Action button
                if facility['status'] == 'available' and not facility.get('blocked', False):
                    book_btn = tk.Button(facility_frame, text="Book Now", 
                                       command=lambda f=facility: self.show_sports_booking_form(f),
                                       bg='#27ae60', fg='white', font=("Arial", 9))
                    book_btn.pack(side='right')
                else:
                    status_msg = "DIBLOKIR" if facility.get('blocked', False) else f"Digunakan: {facility['current_booking']}"
                    tk.Label(facility_frame, text=status_msg, font=("Arial", 9), fg='gray').pack(side='right')
        
        print("✅ Sports dashboard ready")

    def show_sports_booking_form(self, facility):
        """Show sports booking form"""
        booking_window = tk.Toplevel(self.window)
        booking_window.title(f"Booking {facility['name']}")
        booking_window.geometry("500x600")
        booking_window.configure(bg='white')
        booking_window.transient(self.window)
        booking_window.eval('tk::PlaceWindow . center')
        
        tk.Label(booking_window, text=f"BOOKING {facility['name']}", 
                font=("Arial", 16, "bold")).pack(pady=20)
        
        # Facility info
        info_frame = tk.Frame(booking_window)
        info_frame.pack(fill='x', padx=30, pady=10)
        
        tk.Label(info_frame, text=f"Harga: Rp {facility['price']:,} / sesi", 
                font=("Arial", 12, "bold"), fg='green').pack()
        tk.Label(info_frame, text=f"Kapasitas: {facility['capacity']} orang", 
                font=("Arial", 11)).pack()
        
        # Booking form
        form_frame = tk.Frame(booking_window)
        form_frame.pack(fill='x', padx=30, pady=20)
        
        fields = [
            ("Nama Pemesan", "text"),
            ("No. Telepon", "text"),
            ("Jumlah Orang", "number"),
            ("Durasi (sesi)", "number"),
            ("Tanggal Booking", "text"),
            ("Waktu Booking", "text"),
            ("Metode Pembayaran", "combo", self.data['payment_methods'])
        ]
        
        entries = {}
        for field, field_type, *options in fields:
            frame = tk.Frame(form_frame)
            frame.pack(fill='x', pady=8)
            
            tk.Label(frame, text=field, font=("Arial", 11)).pack(anchor='w')
            
            if field_type == 'combo':
                entry = ttk.Combobox(frame, values=options[0], width=27, font=("Arial", 11))
            elif field_type == 'number':
                entry = tk.Spinbox(frame, from_=1, to=10, width=30, font=("Arial", 11))
            else:
                entry = tk.Entry(frame, width=30, font=("Arial", 11), relief='solid', bd=1)
            
            entry.pack(fill='x', pady=5)
            entries[field] = entry
        
        def process_booking():
            # Calculate total price
            duration = int(entries['Durasi (sesi)'].get())
            total_price = facility['price'] * duration
            
            # Create booking
            booking_data = {
                'facility_type': 'sports',
                'facility_name': facility['name'],
                'customer_name': entries['Nama Pemesan'].get(),
                'phone': entries['No. Telepon'].get(),
                'people_count': entries['Jumlah Orang'].get(),
                'duration': duration,
                'total_price': total_price,
                'booking_date': entries['Tanggal Booking'].get(),
                'booking_time': entries['Waktu Booking'].get(),
                'payment_method': entries['Metode Pembayaran'].get(),
                'timestamp': datetime.now().isoformat(),
                'status': 'pending_payment'
            }
            
            self.data['bookings'].append(booking_data)
            
            # If QRIS selected, show payment
            if entries['Metode Pembayaran'].get() == 'QRIS':
                self.show_qris_payment(booking_data)
            else:
                # Update facility status for other methods
                facility['status'] = 'occupied'
                facility['color'] = 'red'
                facility['current_booking'] = entries['Nama Pemesan'].get()
                self.save_data()
                
                self.show_booking_receipt(booking_data, "Sports Facility")
                booking_window.destroy()
                self.show_sports_dashboard()
        
        tk.Button(booking_window, text="💳 Lanjutkan Pembayaran", command=process_booking, 
                 bg='#27ae60', fg='white', font=("Arial", 12), relief='raised', bd=2).pack(pady=20)

    def show_qris_payment(self, booking_data):
        """Show QRIS payment"""
        qris_window = tk.Toplevel(self.window)
        qris_window.title("QRIS Payment")
        qris_window.geometry("400x500")
        qris_window.configure(bg='white')
        qris_window.transient(self.window)
        qris_window.eval('tk::PlaceWindow . center')
        
        tk.Label(qris_window, text="💰 PEMBAYARAN QRIS", font=("Arial", 16, "bold")).pack(pady=20)
        
        # Total amount
        tk.Label(qris_window, text=f"Total: Rp {booking_data['total_price']:,}", 
                font=("Arial", 14, "bold"), fg='green').pack(pady=10)
        
        # QR Code Placeholder
        qr_frame = tk.Frame(qris_window, bg='white', relief='solid', bd=2, width=200, height=200)
        qr_frame.pack_propagate(False)
        qr_frame.pack(pady=20)
        
        tk.Label(qr_frame, text="[QR CODE]\nScan dengan aplikasi\nbank/e-wallet Anda", 
                font=("Arial", 10), bg='white', justify='center').pack(expand=True)
        
        # Instructions
        instructions = [
            "1. Buka aplikasi bank/e-wallet Anda",
            "2. Pilih fitur QRIS",
            "3. Scan kode QR di atas",
            "4. Konfirmasi pembayaran"
        ]
        
        for instruction in instructions:
            tk.Label(qris_window, text=instruction, font=("Arial", 10), justify='left').pack(anchor='w', padx=50, pady=2)
        
        def confirm_payment():
            # Update booking status
            booking_data['status'] = 'confirmed'
            booking_data['payment_status'] = 'paid'
            booking_data['payment_time'] = datetime.now().isoformat()
            
            # Update facility status
            for facility_type in ['swimming_pool', 'gym', 'court']:
                for fac in self.data['sports_facilities'][facility_type]:
                    if fac['name'] == booking_data['facility_name']:
                        fac['status'] = 'occupied'
                        fac['color'] = 'red'
                        fac['current_booking'] = booking_data['customer_name']
                        break
            
            self.save_data()
            
            messagebox.showinfo("Success", "Pembayaran berhasil!")
            qris_window.destroy()
            self.show_booking_receipt(booking_data, "Sports Facility")
            self.show_sports_dashboard()
        
        tk.Button(qris_window, text="✅ Saya Sudah Bayar", command=confirm_payment,
                 bg='#27ae60', fg='white', font=("Arial", 12), relief='raised', bd=2).pack(pady=20)

    def show_booking_receipt(self, booking_data, facility_type):
        """Show booking receipt"""
        receipt_window = tk.Toplevel(self.window)
        receipt_window.title("Booking Receipt")
        receipt_window.geometry("400x500")
        receipt_window.configure(bg='white')
        receipt_window.transient(self.window)
        receipt_window.eval('tk::PlaceWindow . center')
        
        tk.Label(receipt_window, text="✅ BOOKING BERHASIL", font=("Arial", 16, "bold"), fg='green').pack(pady=20)
        
        # Receipt details
        details_frame = tk.Frame(receipt_window)
        details_frame.pack(fill='both', expand=True, padx=30, pady=10)
        
        details = [
            ("No. Booking", f"BK{random.randint(1000, 9999)}"),
            ("Tanggal Booking", datetime.now().strftime("%d/%m/%Y %H:%M")),
            ("Jenis Fasilitas", facility_type),
            ("Nama Fasilitas", booking_data.get('classroom') or booking_data.get('facility_name')),
            ("Nama Pemesan", booking_data.get('customer_name') or booking_data.get('nama_pemesan')),
        ]
        
        if facility_type == "Sports Facility":
            details.extend([
                ("Total Biaya", f"Rp {booking_data['total_price']:,}"),
                ("Metode Pembayaran", booking_data.get('payment_method', 'Cash')),
                ("Status Pembayaran", "LUNAS" if booking_data.get('payment_status') == 'paid' else 'PENDING')
            ])
        
        for label, value in details:
            frame = tk.Frame(details_frame)
            frame.pack(fill='x', pady=5)
            tk.Label(frame, text=f"{label}:", font=("Arial", 10, "bold"), width=15, anchor='w').pack(side='left')
            tk.Label(frame, text=value, font=("Arial", 10)).pack(side='left')
        
        # Save button
        tk.Button(receipt_window, text="💾 Simpan Bukti", 
                 command=lambda: self.save_receipt(booking_data, facility_type),
                 bg='#3498db', fg='white', font=("Arial", 11), relief='raised', bd=2).pack(pady=10)
        
        tk.Button(receipt_window, text="Tutup", command=receipt_window.destroy,
                 bg='#95a5a6', fg='white', font=("Arial", 11), relief='raised', bd=2).pack(pady=5)

    def save_receipt(self, booking_data, facility_type):
        """Save receipt to file"""
        receipt_text = f"""
BUKTI BOOKING - CAMPUS FACILITY SYSTEM
======================================
No. Booking: BK{random.randint(1000, 9999)}
Tanggal: {datetime.now().strftime("%d/%m/%Y %H:%M")}
Jenis: {facility_type}
Fasilitas: {booking_data.get('classroom') or booking_data.get('facility_name')}
Pemesan: {booking_data.get('customer_name') or booking_data.get('nama_pemesan')}
"""
        
        if facility_type == "Sports Facility":
            receipt_text += f"""
Total: Rp {booking_data['total_price']:,}
Metode: {booking_data.get('payment_method', 'Cash')}
Status: {"LUNAS" if booking_data.get('payment_status') == 'paid' else 'PENDING'}
"""
        
        # Save to file
        filename = f"receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(receipt_text)
            messagebox.showinfo("Success", f"Bukti disimpan sebagai: {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan bukti: {e}")

    def show_admin_dashboard(self):
        """Show admin dashboard"""
        print("👨‍💼 Loading admin dashboard...")
        
        # Clear window
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Header
        self.create_header("ADMIN DASHBOARD - SYSTEM MONITORING", '#8e44ad')
        
        # Tab Control
        tab_control = ttk.Notebook(self.window)
        
        # Overview Tab
        overview_tab = ttk.Frame(tab_control)
        self.setup_overview_tab(overview_tab)
        tab_control.add(overview_tab, text="📊 Overview")
        
        # Users Tab
        users_tab = ttk.Frame(tab_control)
        self.setup_users_tab(users_tab)
        tab_control.add(users_tab, text="👥 Users")
        
        # Facilities Tab
        facilities_tab = ttk.Frame(tab_control)
        self.setup_facilities_tab(facilities_tab)
        tab_control.add(facilities_tab, text="🏢 Facilities")
        
        # Logs Tab
        logs_tab = ttk.Frame(tab_control)
        self.setup_logs_tab(logs_tab)
        tab_control.add(logs_tab, text="📋 Logs")
        
        tab_control.pack(expand=True, fill='both', padx=20, pady=20)
        
        print("✅ Admin dashboard ready")

    def setup_overview_tab(self, parent):
        """Setup overview tab"""
        # Statistics
        stats_frame = tk.Frame(parent)
        stats_frame.pack(fill='x', padx=20, pady=10)
        
        stats = [
            ("Total Users", len(self.data['users'])),
            ("Active Classrooms", len([r for r in self.data['academic_facilities']['classrooms'] if not r.get('blocked', False)])),
            ("Total Bookings", len(self.data['bookings'])),
            ("Pending Payments", len([b for b in self.data['bookings'] if b.get('status') == 'pending_payment']))
        ]
        
        for i, (label, value) in enumerate(stats):
            stat_frame = tk.Frame(stats_frame, relief='raised', bd=1, bg='#ecf0f1')
            stat_frame.grid(row=0, column=i, padx=10, pady=10, sticky='nsew')
            tk.Label(stat_frame, text=label, font=("Arial", 10), bg='#ecf0f1').pack(pady=5)
            tk.Label(stat_frame, text=str(value), font=("Arial", 16, "bold"), bg='#ecf0f1').pack(pady=5)
        
        for i in range(4):
            stats_frame.grid_columnconfigure(i, weight=1)

    def setup_users_tab(self, parent):
        """Setup users tab"""
        tk.Label(parent, text="Daftar Pengguna", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Treeview for users
        columns = ('Username', 'Full Name', 'Role', 'Status')
        tree = ttk.Treeview(parent, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        
        # Add users
        for user in self.data['users']:
            tree.insert('', 'end', values=(
                user['username'],
                user['full_name'],
                user['role'],
                'Active'
            ))
        
        tree.pack(fill='both', expand=True, padx=20, pady=10)

    def setup_facilities_tab(self, parent):
        """Setup facilities tab"""
        tk.Label(parent, text="Manajemen Fasilitas", font=("Arial", 14, "bold")).pack(pady=10)
        
        control_frame = tk.Frame(parent)
        control_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(control_frame, text="Pilih Fasilitas untuk Diblokir/Dibuka:", 
                font=("Arial", 11)).pack(anchor='w')
        
        facility_frame = tk.Frame(parent)
        facility_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Academic facilities
        tk.Label(facility_frame, text="Ruang Kelas:", font=("Arial", 12, "bold")).pack(anchor='w', pady=5)
        for classroom in self.data['academic_facilities']['classrooms']:
            var = tk.BooleanVar(value=classroom.get('blocked', False))
            chk = tk.Checkbutton(facility_frame, text=f"{classroom['name']} - {classroom['status']}", 
                               variable=var, font=("Arial", 10),
                               command=lambda c=classroom, v=var: self.toggle_facility_block(c, v))
            chk.pack(anchor='w', padx=20)
        
        # Sports facilities
        tk.Label(facility_frame, text="Fasilitas Olahraga:", font=("Arial", 12, "bold")).pack(anchor='w', pady=(15, 5))
        for category in ['swimming_pool', 'gym', 'court']:
            for facility in self.data['sports_facilities'][category]:
                var = tk.BooleanVar(value=facility.get('blocked', False))
                chk = tk.Checkbutton(facility_frame, text=f"{facility['name']} - {facility['status']}", 
                                   variable=var, font=("Arial", 10),
                                   command=lambda f=facility, v=var: self.toggle_facility_block(f, v))
                chk.pack(anchor='w', padx=20)

    def toggle_facility_block(self, facility, var):
        """Toggle facility block status"""
        facility['blocked'] = var.get()
        facility['color'] = 'gray' if var.get() else 'green'
        self.save_data()
        status = "diblokir" if var.get() else "dibuka"
        messagebox.showinfo("Success", f"Fasilitas {facility['name']} berhasil {status}!")

    def setup_logs_tab(self, parent):
        """Setup logs tab"""
        notebook = ttk.Notebook(parent)
        
        # Login History
        login_tab = ttk.Frame(notebook)
        self.setup_login_logs(login_tab)
        notebook.add(login_tab, text="Login History")
        
        # Booking History
        booking_tab = ttk.Frame(notebook)
        self.setup_booking_logs(booking_tab)
        notebook.add(booking_tab, text="Booking History")
        
        notebook.pack(expand=True, fill='both', padx=10, pady=10)

    def setup_login_logs(self, parent):
        """Setup login logs"""
        columns = ('Username', 'Role', 'Timestamp', 'IP')
        tree = ttk.Treeview(parent, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        for log in self.data['login_history'][-20:]:
            tree.insert('', 'end', values=(
                log['username'],
                log['role'],
                datetime.fromisoformat(log['timestamp']).strftime("%d/%m/%Y %H:%M"),
                log.get('ip_address', 'localhost')
            ))
        
        tree.pack(fill='both', expand=True)

    def setup_booking_logs(self, parent):
        """Setup booking logs"""
        columns = ('Facility', 'Customer', 'Date', 'Time', 'Status', 'Amount')
        tree = ttk.Treeview(parent, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        
        for booking in self.data['bookings'][-20:]:
            amount = f"Rp {booking.get('total_price', 0):,}" if booking.get('total_price') else "-"
            tree.insert('', 'end', values=(
                booking.get('classroom') or booking.get('facility_name'),
                booking.get('customer_name') or booking.get('nama_pemesan'),
                booking.get('booking_date', '-'),
                booking.get('booking_time', '-'),
                booking.get('status', 'unknown'),
                amount
            ))
        
        tree.pack(fill='both', expand=True)

    def logout(self):
        """Logout user"""
        print("🚪 Logging out...")
        self.current_user = None
        self.current_facility_type = None
        messagebox.showinfo("Info", "Logout berhasil!")
        self.show_login_page()

    def run(self):
        """Run the application"""
        print("🎉 Campus Facility System Ready!")
        print("=" * 50)
        self.window.mainloop()

# Run the application
if __name__ == "__main__":
    app = CampusFacilitySystem()
    app.run()
