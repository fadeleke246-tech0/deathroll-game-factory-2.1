"""
🎮 DEATHROLL.CO AUTOMATED GAME FACTORY
Username: fadeleke246-tech0
Email: favouradeleke246@gmail.com
Runs until: 2027-12-31
"""

import os
import json
import random
import datetime
import time
from pathlib import Path

# ==================== CONFIGURATION ====================
CONFIG = {
    "brand": "deathroll.co",
    "email": "favouradeleke246@gmail.com",
    "github_username": "fadeleke246-tech0",
    "target_date": "2027-12-31",
    "daily_games": 3
}

# ==================== FACTORY CLASS ====================
class GameFactory:
    def __init__(self):
        self.base_dir = Path("games")
        self.base_dir.mkdir(exist_ok=True)
        self.today = datetime.datetime.now().strftime("%Y%m%d")
        
    def create_game(self):
        """Create 2D or 3D game"""
        is_3d = random.choice([True, False])
        
        if is_3d:
            game_type = random.choice([
                "First Person Shooter", "Racing Game", "Open World RPG",
                "Survival Horror", "Battle Royale", "Flight Simulator"
            ])
            price = random.randint(49, 349)
            dimension = "3D"
        else:
            game_type = random.choice([
                "2D Platformer", "Puzzle Game", "Top-Down Shooter",
                "Endless Runner", "Strategy Game", "Visual Novel"
            ])
            price = random.randint(29, 149)
            dimension = "2D"
        
        game_id = f"DR{random.randint(1000,9999)}"
        timestamp = datetime.datetime.now().strftime("%H%M%S")
        
        game = {
            "id": game_id,
            "name": f"Deathroll_{dimension}_{game_type.replace(' ', '_')}_{self.today}",
            "dimension": dimension,
            "type": game_type,
            "price": price,
            "created": datetime.datetime.now().isoformat(),
            "email": CONFIG["email"],
            "brand": CONFIG["brand"],
            "github_url": f"https://github.com/{CONFIG['github_username']}/deathroll-game-factory/tree/main/games/{game_id}",
            "payment": f"PayPal ${price} to {CONFIG['email']}"
        }
        
        return game
    
    def save_game(self, game):
        """Save game files"""
        game_dir = self.base_dir / game["id"]
        game_dir.mkdir(exist_ok=True)
        
        # Save game info
        with open(game_dir / "game_info.json", "w") as f:
            json.dump(game, f, indent=2)
        
        # Create README
        readme = self.create_readme(game)
        with open(game_dir / "README.md", "w") as f:
            f.write(readme)
        
        # Create simple game code
        code = self.create_game_code(game)
        with open(game_dir / "game.py", "w") as f:
            f.write(code)
        
        print(f"✅ {game['name']} - ${game['price']}")
        return game_dir
    
    def create_readme(self, game):
        """Create README file"""
        return f"""# {game['name']}
## {game['dimension']} {game['type']} Template
### Created by {CONFIG['brand']} Game Factory

**Game ID:** {game['id']}
**Price:** ${game['price']}
**Created:** {game['created']}
**Contact:** {CONFIG['email']}

## 🎮 What You Get
- Complete source code
- All game assets
- Commercial license
- 30 days support

## 💰 How to Purchase
1. Send ${game['price']} via PayPal to: {CONFIG['email']}
2. Email payment confirmation
3. Receive download link within 24 hours

## 🔗 GitHub
{game['github_url']}

## 📞 Contact
Email: {CONFIG['email']}
Brand: {CONFIG['brand']}

© {datetime.datetime.now().year} {CONFIG['brand']}
"""
    
    def create_game_code(self, game):
        """Create Python game code"""
        return f'''# {game['name']}
# Created by {CONFIG['brand']} Game Factory
# Generated: {game['created']}

print("🎮 {game['name']}")
print("🏷️ Brand: {CONFIG['brand']}")
print("📧 Contact: {CONFIG['email']}")
print("💰 Price: ${game['price']}")
print("=" * 40)

# Game code would go here
def main():
    print("Game starting...")
    score = 0
    
    for i in range(10):
        score += 10
        print(f"Score: {{score}}")
    
    print("Game over!")
    print("Contact {CONFIG['email']} for full source code")

if __name__ == "__main__":
    main()
'''
    
    def run_daily(self):
        """Run daily factory"""
        print("\n" + "="*60)
        print(f"🚀 DEATHROLL GAME FACTORY")
        print(f"👤 GitHub: {CONFIG['github_username']}")
        print(f"📧 Email: {CONFIG['email']}")
        print(f"📅 Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("="*60)
        
        games = []
        total_value = 0
        
        for i in range(CONFIG["daily_games"]):
            print(f"\n🎮 Creating game {i+1}...")
            game = self.create_game()
            self.save_game(game)
            games.append(game)
            total_value += game["price"]
        
        # Create report
        report = {
            "date": datetime.datetime.now().isoformat(),
            "github_user": CONFIG["github_username"],
            "email": CONFIG["email"],
            "games_created": len(games),
            "total_value": total_value,
            "games": games
        }
        
        os.makedirs("reports", exist_ok=True)
        report_file = f"reports/daily_{self.today}.json"
        with open(report_file, "w") as f:
            json.dump(report, f, indent=2)
        
        print("\n" + "="*60)
        print("📊 DAILY SUMMARY")
        print("="*60)
        print(f"Games created: {len(games)}")
        print(f"Total value: ${total_value}")
        print(f"Contact for sales: {CONFIG['email']}")
        print(f"GitHub: https://github.com/{CONFIG['github_username']}")
        print("="*60)
        
        return games

# ==================== RUN FACTORY ====================
def main():
    """Main execution"""
    print("🎮 Initializing Deathroll Game Factory...")
    print(f"👤 GitHub: fadeleke246-tech0")
    print(f"📧 Email: favouradeleke246@gmail.com")
    print(f"🏷️ Brand: deathroll.co")
    print(f"🎯 Running until: 2027-12-31")
    
    # Create factory and run
    factory = GameFactory()
    games = factory.run_daily()
    
    print(f"\n✅ FACTORY RUN COMPLETE!")
    print(f"📁 Check: games/ folder")
    print(f"📧 Check: {CONFIG['email']} for sales")
    print(f"🔗 GitHub: https://github.com/fadeleke246-tech0/deathroll-game-factory")
    
    return games

if __name__ == "__main__":
    main()
