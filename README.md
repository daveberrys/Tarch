<div align="center">
  <img src="/other/TARCH LOGO.png" alt="Tarch Logo" width="128" height="128" />
  <h1>Tarch</h1>
  <span>Yet another Arch Linux distro but for workstations.</span>
</div>

# Awesome Previews
<table>
  <tr>
    <td><img src="/other/preview/previewcli.png" alt="Tarch Preview" /></td>
    <td><img src="/other/preview/previewlabwc.png" alt="Tarch Preview" /></td>
  </tr>
</table>

**Pre-configured Arch Linux distro**, **with a focus of work, gaming, and productivity**. We kept the dotfiles **minimal**, and **less-distracting**. Here are the list and the reason why we use them.
| Package | Reason |
| - | - | 
| nix | Package manager for managing system packages. More secure and has more packages available. |
| kitty | Greatest terminal emulator that I've ever used by far. |
| labwc | Lightweight window manager that is easy to configure and use. |
| waybar | A simple status bar that's perfect for Tarch. |
| zed | A modern yet lightweight text editor for daily coding usage. |
| mpv | Media player. Don't know what else to say. |
| grim & satty | Advanced screenshotting tool. |
| zsh | Generally good shell for scripting and command-line usage. |
| cava | Audio visualization tool for waybar. |
| mako | Lightweight notification display. |
| helium | A lightweight yet greatest web browser. |

## Why switch to Tarch?
Why are you asking me? You should be asking yourself that. Jokes aside, main reason why you'd consider switching to Tarch is;
- Your system is running slow or you're experiencing performance issues.
- You want something new and fresh that's easy to configure and use.
- You want something new and/or fresh
- You hate microslop (common nowadays)

## Why you shouldn't use Tarch
Look, it might not be for you. So here's the reason why you don't want to use it;
- You don't like Arch Linux. (valid)
- You're not comfortable with the command line.
- You like your system to be bloated and slow.
- You're not a fan of systemd.
- You like your current system better.

# Installation
We don't have a github actions or release yet. But we do plan one! If you decide to use this distro, here are the steps to compile from scratch;
- **Step 1**:
  - Use Arch Linux.
    - Yes I'm not kidding. You will need Arch Linux for this.
    - So, boot up your Arch Linux VM or use Distro box!
- **Step 2**:
  - Install `archiso` by doing `sudo pacman -S archiso`
    - This is what I use to compile the ISO.
- **Step 3**:
  - Clone the repository: `git clone https://github.com/daveberry/Tarch`
- **Step 4**:
  - Navigate to the repository directory: `cd Tarch`
  - Run `bash rebuild.sh` to build the iso.
- **Step 5**:
  - Once the build is complete, the ISO will be available in the `out` directory.

Congrats! You have successfully compiled Tarch from scratch. *wait... this isn't linux from scratch...*

## What to do after building the ISO?
You boot into it! In the live environment, you have 3 commands;
- `labwc` - tests my configuration first!
- `tarchinstall` - installs Tarch to your system
- `fastfetch` - shows system information

## What to do after installing Tarch in my system?
Assuming you only did the following;
- Disk Configuration
- Authentication
- Network configuration
- Exiting from Archinstall instead of rebooting
> (which is the **reccomended** path since this already has a config file and also a desktop environment installed)

Here's what you need to do **after installing** Tarch;
- To get into the desktop environment, run `labwc`
> [!NOTE]
> Q: Why do we have to run a command instead of just booting into the desktop environment?
>
> A: For starters, I'm stupid and I don't know how to make it where when you're signed in, you get automatically get booted into labwc. I'll find a way, maybe later or sooner. If you wish to help, feel free to make a issue on what package I should use or submitting a PR.

# Keybinds & Other Stuff.
**Here are all the keybinds**;
```
== General ==
Closing Apps = Super + W
Maximize = Super + Shift + F
Fullscreen = Super + F
Switch desktop 1 to desktop 5 = Super + {1,2,3,4,5}
Switch windows = Alt + Tab, Alt + Shift + Tab
Reload LabWC = Super + Ctrl + R

== Apps ==
Open Nautilus (File Explorer) = Super + E
Open Ranger (File Backup Explorer) = Super + Shift + E
Open Kitty (Terminal) = Super + Enter
Open Rofi App lists = Super + D
Open Rofi Power lists = Super + Shift + Ctrl + S
Open System Controls = Super + S
```

**Here's some other stuff you should know**;
- We obviously use the `nix` package manager. But we added alias!
  - install package; nixpi
  - remove package; nixpr
  - search package; nixps
  - update package; nixpu
- We don't use the Arch User Repository. We use the `nixpkgs` package repository. https://search.nixos.org/packages
- You still can use `pacman`! Only the repositores `core` and `extra` is included.

---

# Support the Project
I got nothing. Just starring the repository or [joining my Discord server](https://discord.gg/S5jTpsq8Js) and giving me tips and feedback could help with the development.

# Built with
- [Zed Editor](https://zed.dev/)
- [ArchISO](https://wiki.archlinux.org/title/Archiso)

# Contributing
[CONTRIBUTING.md](CONTRIBUTING.md)

# License
[MIT LICENSE](LICENSE)