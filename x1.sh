#!/data/data/com.termux/files/usr/bin/bash

clear

# ==============================
# X1 VULN SCANNER
# Terminal UI
# ==============================

animate() {
    frames=(
        "[        ]"
        "[=       ]"
        "[==      ]"
        "[===     ]"
        "[====    ]"
        "[=====   ]"
        "[======  ]"
        "[======= ]"
        "[========]"
    )

    for frame in "${frames[@]}"; do
        printf "\r[*] Initializing X1 %s" "$frame"
        sleep 0.08
    done

    printf "\n"
}

banner() {
    echo
    echo "╔══════════════════════════════════════════════╗"
    echo "║                                              ║"
    echo "║              ██╗  ██╗ ██╗                   ║"
    echo "║              ╚██╗██╔╝ ██║                   ║"
    echo "║               ╚███╔╝  ██║                   ║"
    echo "║               ██╔██╗  ██║                   ║"
    echo "║              ██╔╝ ██╗ ██║                   ║"
    echo "║              ╚═╝  ╚═╝ ╚═╝                   ║"
    echo "║                                              ║"
    echo "║              X1 VULN SCANNER                ║"
    echo "║              Security Auditor               ║"
    echo "║                                              ║"
    echo "╚══════════════════════════════════════════════╝"
    echo
}

startup() {
    animate
    sleep 0.2

    echo "[✓] Loading scanner..."
    sleep 0.15

    echo "[✓] Loading security checks..."
    sleep 0.15

    echo "[✓] Loading report engine..."
    sleep 0.15

    echo "[✓] X1 Scanner ready."
    sleep 0.5
}

menu() {
    while true; do
        clear
        banner

        echo "              X1 MAIN MENU"
        echo
        echo "  [1] Scan Target"
        echo "  [2] View Reports"
        echo "  [3] Scanner Information"
        echo "  [4] Settings"
        echo "  [5] Exit"
        echo
        printf "  X1 > "

        read -r choice

        case "$choice" in
            1)
                clear
                banner
                echo "[*] Scan Target"
                echo
                read -r -p "Target URL: " target

                if [ -z "$target" ]; then
                    echo
                    echo "[!] Target cannot be empty."
                    sleep 1.5
                    continue
                fi

                echo
                python3 main.py "$target"

                echo
                read -r -p "Press Enter to return to menu..."
                ;;

            2)
                clear
                banner
                echo "[*] Reports"
                echo

                if [ -d "reports" ]; then
                    ls -lah reports
                else
                    echo "[!] Reports directory not found."
                fi

                echo
                read -r -p "Press Enter to return to menu..."
                ;;

            3)
                clear
                banner
                echo "[*] X1 VULN SCANNER"
                echo
                echo "Version : 1.0"
                echo "Engine  : Python"
                echo "UI      : Bash"
                echo "Platform: Termux / Linux"
                echo
                echo "Modules:"
                echo "  - HTTP Scanner"
                echo "  - Security Headers"
                echo "  - Cookie Analyzer"
                echo "  - Finding Engine"
                echo "  - Report System"
                echo
                read -r -p "Press Enter to return to menu..."
                ;;

            4)
                clear
                banner
                echo "[*] Settings"
                echo
                echo "Settings module is not available yet."
                echo
                read -r -p "Press Enter to return to menu..."
                ;;

            5)
                clear
                echo
                echo "[*] Shutting down X1..."
                sleep 0.5
                echo "[✓] Goodbye."
                sleep 0.5
                clear
                exit 0
                ;;

            *)
                echo
                echo "[!] Invalid option."
                sleep 1
                ;;
        esac
    done
}

startup
menu
