#!/bin/bash
echo "[+] Updating package lists..."
pkg update -y
echo "[+] Installing Python and Git..."
pkg install python git -y
echo "[+] Creating reports directory..."
mkdir -p reports
echo "[+] Setup completed successfully!"
