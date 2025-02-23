import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset (or train a simple model)
dataset = [
    # High Conspiracy Scores (80-100)
    ("Breaking: Alien Invasion Confirmed!", 95),
    ("Secret Government Lab Creating Super Soldiers!", 90),
    ("The Moon Landing Was Faked!", 85),
    ("Elites Controlling Weather With Hidden Technology!", 92),
    ("Time Travel Machine Discovered in Area 51!", 97),
    ("NASA Hiding Evidence of Extraterrestrial Life!", 93),
    ("Chemtrails Are Spreading Mind-Control Substances!", 89),
    ("Flat Earth Theory Gains New Evidence!", 87),
    ("Ancient Pyramids Built by Aliens!", 88),
    ("Illuminati Controlling the Global Economy!", 94),
    ("New World Order Plans to Take Over Governments!", 96),
    ("Microchips in Vaccines: The Truth Revealed!", 91),
    ("Secret Underground Cities Discovered!", 98),
    ("AI Robots Conspiring Against Humanity!", 95),
    ("Hollywood Actors Are Clones Controlled by the Elite!", 88),
    ("Reptilian Overlords Secretly Rule the World!", 97),
    ("Scientists Hiding Proof of Parallel Universes!", 90),
    ("Hidden Cures for Cancer Kept Secret by Big Pharma!", 93),
    ("UFO Sighting Covered Up by Military!", 92),
    ("Hollow Earth Theory Gains Scientific Backing!", 89),
    ("Global Leaders Secretly Meet to Plan Mass Surveillance!", 97),
    ("Television Signals Contain Hidden Brainwashing Frequencies!", 96),
    ("Mysterious Black Helicopters Spotted Over Major Cities!", 95),
    ("Underground Bunkers Being Built for the Elite!", 98),
    ("Time Travelers Spotted at Historical Events!", 94),
    ("Government Releases Mind-Control Chemicals in Drinking Water!", 95),
    ("Alien DNA Experiment Gone Wrong, Scientists Warn!", 93),
    ("Secret Space Fleet Operating Without Public Knowledge!", 91),
    ("Mind Control Chips Are Being Implanted in Children!", 92),
    ("Secret Lab Discovers Immortality Serum, But It's Only for the Rich!", 98),
    ("New Evidence Suggests Elvis Presley is Alive!", 89),
    ("Deep State Operatives Controlling Global Media!", 94),

    # Moderate Conspiracy Scores (50-79)
    ("New Research Suggests Vaccines May Have Side Effects", 60),
    ("Mysterious Signals Detected From Deep Space", 65),
    ("Ancient Civilizations May Have Had Advanced Technology", 55),
    ("Could Artificial Intelligence Become Self-Aware?", 50),
    ("5G Networks: Are They Safe?", 58),
    ("New UFO Sightings Reported Near Military Bases", 62),
    ("Are Cryptocurrencies a Tool for the Global Elite?", 57),
    ("Secret Government Files on UFOs Declassified", 67),
    ("Is There Life on Mars? Scientists Debate", 52),
    ("Mysterious Crop Circles Appear Overnight", 61),
    ("AI-Powered Drones Spotted in Restricted Areas", 66),
    ("Black Holes Could Be Portals to Other Dimensions", 70),
    ("Scientists Discover Strange Object at Bottom of the Ocean", 68),
    ("Reports of Mysterious Disappearances in the Bermuda Triangle", 63),
    ("Research Shows Mind Control Experiments in the 1970s", 74),
    ("Autonomous Cars Might Be Used for Surveillance", 72),
    ("Deepfake Technology Could Be Used for Political Manipulation", 58),
    ("Whistleblower Claims Secret Space Program Exists", 73),
    ("Scientists Discover Possible Ancient Megastructure in Space", 65),
    ("Government Scientists Working on Human Genetic Modification", 71),
    ("Possible Signs of a Hidden Planet Beyond Pluto", 69),
    ("Some Scientists Believe Telepathy Could Be Real", 64),
    ("New Study Links Artificial Sweeteners to Unusual Behavior", 55),
    ("Researchers Claim to Have Found Evidence of a Lost Continent", 58),
    ("Evidence of a 12,000-Year-Old Advanced Civilization Found", 59),
    ("Can the Human Brain Be Hacked with Sound Waves?", 66),
    ("Studies Suggest Time Perception Can Be Manipulated", 70),
    ("Will AI Replace Human Artists Completely?", 62),
    ("Secret Society Influence in Politics Could Be Stronger Than Thought", 73),
    ("Is There a Hidden Underground Ocean on Earth?", 67),
    ("Lost City Discovered Beneath the Amazon Jungle", 71),

    # Low Conspiracy Scores (0-49)
    ("Government Approves New Tax Policy", 10),
    ("Scientists Discover a New Particle", 20),
    ("Stock Market Reaches Record High", 15),
    ("Medical Breakthrough: New Cancer Treatment Shows Promise", 8),
    ("Technology Giants Announce AI Partnership", 12),
    ("SpaceX Successfully Launches New Rocket", 5),
    ("Major League Finals: Exciting Match Ends in Victory", 7),
    ("Global Leaders Meet for Climate Change Summit", 9),
    ("New Study Reveals Health Benefits of Mediterranean Diet", 14),
    ("Advancements in Quantum Computing Announced by Researchers", 18),
    ("NASA Plans New Manned Mission to the Moon", 11),
    ("Tech Companies Invest Billions in Renewable Energy", 13),
    ("Scientists Discover a New Species of Marine Life", 6),
    ("Olympic Games Set to Break Records This Year", 4),
    ("Electric Cars Expected to Dominate the Market by 2030", 17),
    ("Breakthrough in Alzheimer’s Research Brings Hope", 16),
    ("International Space Station Crew Conducts Successful Experiment", 3),
    ("World Health Organization Recommends New Dietary Guidelines", 12),
    ("New AI Model Predicts Climate Patterns More Accurately", 19),
    ("Scientists Develop Biodegradable Plastics to Reduce Pollution", 8),
    ("Researchers Discover Oldest Fossil of Human Ancestor", 22),
    ("Health Officials Recommend Increased Exercise for Longevity", 21),
    ("Apple Unveils Latest iPhone Model with Improved Camera", 10),
    ("New Traffic Regulations Aim to Reduce Accidents", 13),
    ("Education Reform Bill Passes in Parliament", 12),
    ("New Study Confirms Benefits of Meditation on Brain Health", 14),
    ("Sports Scientists Develop Training Program to Reduce Injuries", 18),
    ("New COVID Variant Detected, Experts Say No Cause for Panic", 16),
    ("Solar Panel Efficiency Reaches New Milestone", 9),
    ("Mathematicians Solve Decades-Old Equation", 20),
    ("Local Startup Creates Revolutionary AI-Powered Health App", 15),
]


# Train a TF-IDF model for simple classification
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform([news[0] for news in dataset])
y_train = [news[1] for news in dataset]

model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
import os

# Ensure the models directory exists
models_dir = os.path.dirname("backend/models/model.pkl")
os.makedirs(models_dir, exist_ok=True)

# Save the trained model and vectorizer
joblib.dump(model, "backend/models/model.pkl")
joblib.dump(vectorizer, "backend/models/vectorizer.pkl")


# Prediction Function
def predict_conspiracy_score(headline):
    """Predicts the conspiracy score of a given headline."""
    model = joblib.load("backend/models/model.pkl")
    vectorizer = joblib.load("backend/models/vectorizer.pkl")
    transformed_text = vectorizer.transform([headline])
    score = model.predict(transformed_text)[0]
    return round(score, 2)

 # Step 5: Test the Model
if __name__ == "__main__":
    test_headline = "Aliens are taking over the world!"
    print(f"Headline: {test_headline}")
    print(f"Predicted Conspiracy Score: {predict_conspiracy_score(test_headline)}")
