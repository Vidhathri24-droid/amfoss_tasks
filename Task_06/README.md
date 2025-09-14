
# Friendly Neighborhood Bot  

A Discord bot for **Midtown Tech**, inspired by Spider-Man’s friendly neighborhood spirit. 
It welcomes new members, moderates chaos, posts timed announcements, and shares quick wisdom. 

---

##  Features
- **Welcome & Orientation** 
  - Greets new members in `#orientation`. 
  - Assigns the role **Aspiring Hero** automatically. 

- **Spider-Sense Moderation** 
  - Deletes messages with forbidden keywords. 
  - Politely DMs the offender with a warning. 

- **Daily Bugle Announcements** 
  - `!bugle <message>` posts announcements in `#announcements`. 
  - Deletes them after 24h unless pinned. 

- **Aunt May’s Wisdom** 
  - `!wisdom rules` / `!wisdom resources` / `!wisdom contact`. 

---

##  Setup Guide

### 1. Create a Bot in Discord Developer Portal
1. Go to  [Discord Developer Portal](https://discord.com/developers/applications). 
2. Click **New Application** → give it a name (e.g., `FriendlyNeighborhoodBot`). 
3. In the left menu, go to **Bot** → Click **Add Bot** → Confirm. 
4. Copy your **bot token** (keep it secret). 

---

### 2. Enable Privileged Intents
1. In the **Bot** settings, scroll to **Privileged Gateway Intents**. 
2. Enable:
   - **Server Members Intent** (for welcome/roles). 
   - **Message Content Intent** (for moderation). 
3. Save changes. 

---

### 3. Invite the Bot to Your Server
1. Go to **OAuth2 → URL Generator**. 
2. Under **Scopes**, select `bot`. 
3. Under **Bot Permissions**, enable:
   - Manage Roles 
   - Manage Messages 
   - Read Messages/View Channels 
   - Send Messages 
   - Read Message History 
   - Embed Links 
4. Copy the generated link → Open in your browser → Invite bot to your server. 

---

### 4. Install Requirements
Make sure you have **Python 3.9+** installed. 

```bash
pip install discord.py
```

---

### 5. Run the Bot
Save the bot script as `bot.py`. Replace `YOUR_BOT_TOKEN` with your actual token. 

Run it with: 
```bash
python bot.py
```

If successful, the bot will appear **online** in your server. 

---

##  Commands
- `!bugle <message>` → Post announcement (Faculty/Admin only). 
- `!wisdom rules` → Show rules. 
- `!wisdom resources` → Show resources. 
- `!wisdom contact` → Show contact info. 

---

##  Project Structure
```
friendly-neighborhood-bot/
│── bot.py         # main bot script
│── README.md      # setup guide (this file)
```

---

##  Important Notes
- Never share your **bot token**. If leaked, reset it in Developer Portal. 
- This bot uses **in-memory timers** → announcements won’t survive bot restarts. 
- Make sure your bot role is **above** the role it needs to assign (`Aspiring Hero`). 
