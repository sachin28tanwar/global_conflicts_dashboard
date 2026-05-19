import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Global Conflicts Explorer", layout="wide", page_icon="🌍")

# --- DATA PREPARATION ---

# 1. Expanded Historical Wars Data
historical_wars_data = {
    "War": [
        "World War II", "Mongol Conquests", "Taiping Rebellion", "World War I", 
        "Second Sino-Japanese War", "Russian Civil War", "Thirty Years' War", 
        "Napoleonic Wars", "Korean War", "Vietnam War", "Iran-Iraq War", 
        "Rwandan Genocide", "American Civil War", "Spanish Civil War", "The Crusades"
    ],
    "Start Year": [1939, 1206, 1850, 1914, 1937, 1917, 1618, 1803, 1950, 1955, 1980, 1994, 1861, 1936, 1095],
    "End Year": [1945, 1368, 1864, 1918, 1945, 1922, 1648, 1815, 1953, 1975, 1988, 1994, 1865, 1939, 1291],
    "Military Casualties": [24000000, 5000000, 3000000, 9700000, 4000000, 1200000, 2000000, 2500000, 1200000, 1300000, 500000, 0, 620000, 200000, 1000000],
    "Civilian Casualties": [50000000, 35000000, 17000000, 10000000, 18000000, 8000000, 6000000, 1000000, 1500000, 2000000, 500000, 800000, 50000, 300000, 2000000]
}
df_historical = pd.DataFrame(historical_wars_data)
df_historical["Total Casualties"] = df_historical["Military Casualties"] + df_historical["Civilian Casualties"]

# 2. Expanded Historical Map Data
map_data = {
    "Event": [
        "Battle of Stalingrad", "Auschwitz Extermination", "Hiroshima Bombing", 
        "Nanjing Massacre", "Battle of Verdun", "Battle of the Somme", "Siege of Baghdad", 
        "Battle of Gettysburg", "Battle of Waterloo", "Siege of Jerusalem", "Tet Offensive (Hue)",
        "Bombing of Dresden", "Gallipoli Campaign", "Kigali Massacre", "Guernica Bombing"
    ],
    "Conflict": [
        "World War II", "World War II", "World War II", 
        "WWII (Sino-Japanese)", "World War I", "World War I", "Mongol Conquests", 
        "American Civil War", "Napoleonic Wars", "First Crusade", "Vietnam War",
        "World War II", "World War I", "Rwandan Genocide", "Spanish Civil War"
    ],
    "Lat": [48.70, 50.03, 34.38, 32.06, 49.16, 50.01, 33.31, 39.83, 50.68, 31.76, 16.46, 51.05, 40.24, -1.94, 43.31],
    "Lon": [44.51, 19.17, 132.45, 118.79, 5.38, 2.68, 44.36, -77.23, 4.41, 35.21, 107.59, 13.73, 26.28, 30.06, -2.67],
    "Casualties": [2000000, 1100000, 140000, 300000, 700000, 1000000, 800000, 50000, 50000, 40000, 10000, 25000, 500000, 250000, 1600],
    "Description": [
        "The deadliest battle in human history. Brutal urban warfare.",
        "The largest Nazi concentration and extermination camp.",
        "The first use of an atomic weapon in warfare.",
        "Mass murder and systematic rape by Imperial Japanese troops.",
        "A 300-day WWI battle defined by relentless artillery fire.",
        "Over 1 million casualties in muddy, trench-warfare slaughter.",
        "The destruction of the Abbasid Caliphate by Mongol forces.",
        "The bloodiest battle of the American Civil War.",
        "The final defeat of French Emperor Napoleon Bonaparte.",
        "Massacre of the city's inhabitants following the Crusader breach.",
        "Fierce urban combat and civilian massacres during the Vietnam War.",
        "Firebombing by Allied forces that incinerated the city center.",
        "A disastrous Allied amphibious assault against the Ottoman Empire.",
        "The epicenter of the 100-day genocide against the Tutsi.",
        "Aerial terror bombing of civilians, inspiring Picasso's famous painting."
    ]
}
df_map_historical = pd.DataFrame(map_data)

# 3. Current Conflicts Data (May 2026)
current_map_data = {
    "Hotzone": [
        "Kharkiv & Chasiv Yar", "Tehran & Isfahan", "Gaza Strip", 
        "El Fasher, Darfur", "Khartoum, Sudan", "Yangon & Shan State", 
        "Goma, DRC", "Red Sea Chokepoint"
    ],
    "Conflict": [
        "Russo-Ukrainian War", "2026 Middle East Escalation", "Gaza-Israel Conflict",
        "Sudan Civil War", "Sudan Civil War", "Myanmar Civil War", 
        "Kivu Conflict", "Houthi Maritime Crisis"
    ],
    "Lat": [49.99, 32.65, 31.40, 13.62, 15.50, 21.00, -1.65, 14.55],
    "Lon": [36.23, 51.66, 34.35, 25.35, 32.55, 98.00, 29.22, 42.10],
    "Intensity Level (1-10)": [10, 8, 9, 10, 9, 8, 7, 7],
    "Situation": [
        "Massive artillery and glide-bomb devastation; trench warfare attrition.",
        "High-altitude air defense interceptions; targeted infrastructure strikes.",
        "Total urban destruction, mass displacement, and humanitarian collapse.",
        "RSF siege causing widespread famine and targeted ethnic massacres.",
        "Capital city reduced to a wasteland by warring military factions.",
        "Junta airstrikes on civilian villages; rapid rebel territorial gains.",
        "M23 rebel siege displacing millions into squalid camps.",
        "Anti-ship ballistic missiles striking commercial freighters."
    ]
}
df_current_map = pd.DataFrame(current_map_data)


# --- UI HEADER ---
st.title("🌍 Global Conflicts & The Cost of War")

# Sentimental Objective Statement
st.markdown("""
> *"The death of one man is a tragedy. The death of millions is a statistic."*

**Welcome to this digital memorial.** 

This dashboard was not built to celebrate victories, analyze military strategies, or glorify the shifting of borders. It was created with a solemn, singular objective: **to make us profoundly aware of the sheer loss of human life and the catastrophic destruction left in the wake of warfare.**

Behind every data point on these maps, every bar on these charts, and every casualty count lies a shattered family, a lost generation, and a ruined home. As you navigate through the atrocities of our history and the active warzones of our present day, we ask you to reflect on the staggering physical and psychological toll of conflict. 

By visualizing the brutal realities of war—stripping away the politics to reveal the true cost borne by the "common folk"—we hope to serve as a stark reminder of the tragic price of our collective failures to find peace.
""")
st.divider()

# --- TABS REORGANIZED ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📍 Historical Brutality Map", 
    "🚨 Current Conflicts (2026)", 
    "📖 Historical Events & Destruction", 
    "📊 Macro Casualty Analytics"
])

# --- TAB 1: HISTORICAL INTERACTIVE MAP ---
with tab1:
    st.header("Interactive Map of Historical Brutality")
    st.markdown("""
    This map highlights specific locations that experienced extreme wartime destruction. 
    **Marker size and color intensity represent the scale of casualties.** Zoom in and hover to view the tragic details of each location.
    """)
    
    fig_hist = px.scatter_mapbox(
        df_map_historical, lat="Lat", lon="Lon", hover_name="Event", 
        hover_data={"Lat": False, "Lon": False, "Conflict": True, "Casualties": True, "Description": True},
        size="Casualties", color="Casualties", color_continuous_scale=px.colors.sequential.YlOrRd,
        size_max=45, zoom=1.5, mapbox_style="carto-darkmatter"
    )
    fig_hist.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=600)
    st.plotly_chart(fig_hist, use_container_width=True)


# --- TAB 2: CURRENT CONFLICTS (2026) ---
with tab2:
    st.header("Active Global Warzones (May 2026)")
    st.markdown("The interactive map below shows the most intense theaters of war currently active. The world is experiencing the highest number of state-based and non-state conflicts since the end of the Cold War, with millions currently displaced.")

    # Current Conflicts Map
    fig_curr = px.scatter_mapbox(
        df_current_map, lat="Lat", lon="Lon", hover_name="Hotzone", 
        hover_data={"Lat": False, "Lon": False, "Conflict": True, "Intensity Level (1-10)": True, "Situation": True},
        size="Intensity Level (1-10)", color="Intensity Level (1-10)", color_continuous_scale=px.colors.sequential.Inferno,
        size_max=25, zoom=2, mapbox_style="carto-darkmatter"
    )
    fig_curr.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=500)
    st.plotly_chart(fig_curr, use_container_width=True)

    st.divider()
    st.subheader("In-Depth Look at Major 2026 Conflicts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🇺🇦 Russo-Ukrainian War (Escalation & Attrition)")
        st.markdown("""
        Moving into its fifth year since the 2022 full-scale invasion, the war in Ukraine has transformed into a hyper-technological meat grinder. 
        * **The Drone War:** The skies are saturated with First-Person View (FPV) kamikaze drones. Infantry cannot move above ground during daylight without being hunted by thermal-equipped quadcopters. 
        * **Trench Warfare:** The Eastern front (Donbas) resembles World War I. Soldiers endure freezing conditions, rats, and endless artillery barrages. "Meat assaults"—sending waves of poorly trained infantry to overwhelm defenses—have resulted in hundreds of thousands of casualties.
        * **Infrastructure Warfare:** Systemic bombing campaigns targeting the power grid have plunged major cities into darkness, creating a constant struggle for heat, water, and survival among civilians.
        """)
        
        st.markdown("#### 🇸🇩 Sudan Civil War (The Silent Catastrophe)")
        st.markdown("""
        The conflict between the Sudanese Armed Forces (SAF) and the paramilitary Rapid Support Forces (RSF) has triggered the worst humanitarian crisis of the decade.
        * **Capital in Ruins:** Khartoum, once a thriving metropolis, has been reduced to an apocalyptic shell of looted buildings and burnt infrastructure.
        * **Darfur Massacres:** In the western region of Darfur, the RSF has conducted targeted ethnic cleansing against non-Arab communities, trapping millions in besieged cities like El Fasher.
        * **Engineered Famine:** Warring factions deliberately block aid convoys, leading to man-made famine conditions threatening over 15 million people with starvation.
        """)

    with col2:
        st.markdown("#### 🇮🇷 2026 Middle East Escalation")
        st.markdown("""
        What began as regional proxy skirmishes has escalated into direct multi-state confrontations involving Iran, Israel, and the United States.
        * **Strategic Strikes:** Preemptive strikes targeted Iranian air defenses, missile silos, and nuclear enrichment infrastructure, triggering massive retaliatory waves of ballistic missiles aimed at population centers.
        * **The Axis of Resistance:** Hezbollah in Lebanon, militias in Iraq, and the Houthis in Yemen have launched coordinated swarm attacks, overwhelming advanced iron dome and laser defense systems.
        * **Maritime Blockade:** The Red Sea and Strait of Hormuz have become militarized zones, with anti-ship missiles severely restricting global trade and threatening energy security.
        """)
        
        st.markdown("#### 🇲🇲 Myanmar Civil War (Operation 1027)")
        st.markdown("""
        Following the 2021 military coup, resistance groups (the PDF) and ethnic armed organizations formed an unprecedented alliance against the Junta.
        * **Junta Airstrikes:** Losing ground daily, the military junta has resorted to punitive airstrikes and thermobaric bombing of civilian villages, hospitals, and schools to punish rebel sympathizers.
        * **Urban Guerrilla Warfare:** Fighting has reached the outskirts of major cities. Conscription laws have forced thousands of youths to flee into the jungle, fueling a brutal, close-quarters insurgency against a deeply entrenched military dictatorship.
        """)


# --- TAB 3: HISTORICAL EVENTS & DESTRUCTION ---
with tab3:
    st.header("The Visceral Reality of War: Ruin and Destruction")
    
    # WWII Section
    st.subheader("World War II: Industrial Slaughter and The Holocaust")
    st.markdown("""
    **The Mechanization of Genocide**  
    The Holocaust was not merely a massacre; it was the chilling application of industrial bureaucracy to human extermination. The *Einsatzgruppen* (mobile death squads) initially roamed Eastern Europe, executing over a million people into mass pits. Seeking a more "efficient" and psychologically detached method, the Nazi regime built extermination camps like Auschwitz, Treblinka, and Belzec.
    
    Victims were crammed into cattle cars without food or water for days. Upon arrival, SS doctors conducted selections. The elderly, pregnant women, and young children were sent directly to gas chambers disguised as shower rooms. Zyklon B (hydrogen cyanide) was dropped through roof vents, killing thousands in agonizing panic within 20 minutes. Their bodies were then burned in massive crematoria, filling the sky with human ash.
    
    **The Eastern Front and Strategic Bombing**  
    On the Eastern Front, the war was one of absolute annihilation. The Siege of Leningrad lasted 872 days, resulting in over a million civilian deaths primarily from starvation—citizens were forced to eat wallpaper paste, leather, and eventually each other. In the skies over Europe and Japan, strategic bombing campaigns firebombed cities like Dresden, Hamburg, and Tokyo. The incendiary bombs created "firestorms"—hurricanes of fire that sucked oxygen from the air and reached temperatures that melted asphalt and boiled people alive in underground shelters.
    """)

    st.divider()

    # WWI Section
    st.subheader("World War I: The Mud, Gas, and the Meat Grinder")
    st.markdown("""
    **The Trench Hellscape**  
    The Western Front devolved into an unrecognizable nightmare of mud, barbed wire, and craters. Soldiers lived in trenches filled with freezing water, human waste, and unburied corpses. The conditions led to "Trench Foot," a fungal infection that caused tissue to rot away, often requiring amputation. 
    
    **Chemical Warfare and Shell Shock**  
    WWI introduced chemical weapons. Chlorine gas drowned men from the inside out as their lungs filled with fluid. Mustard gas burned the skin and blinded its victims, condemning survivors to a lifetime of agony. The psychological toll was equally devastating. Constant, deafening artillery barrages—sometimes lasting for weeks—shattered men's minds, resulting in "Shell Shock" (now known as PTSD). Men would be left trembling violently, unable to speak, or weeping uncontrollably, yet were often executed by their own commanders for "cowardice."
    """)

    st.divider()

    # Civil War Section
    st.subheader("The American Civil War: Medical Horrors and Scorched Earth")
    st.markdown("""
    **Battlefield Medicine**  
    More soldiers died from disease and botched medicine than from bullets. The introduction of the 'Minié ball'—a heavy lead bullet that flattened on impact—shattered bones beyond repair. Because germ theory was not yet understood, surgeons operated in blood-soaked aprons using unwashed saws. Amputation was the standard treatment, performed without antibiotics and often without anesthesia, leading to massive rates of fatal gangrene.
    
    **Prison Camps and Total War**  
    Prisoner-of-war camps were death traps. The Confederate Andersonville prison was an overcrowded, open-air stockade where men drank from a creek that doubled as a latrine. Nearly 13,000 Union soldiers died there from scurvy, dysentery, and sheer starvation, reducing men to living skeletons. By the war's end, the Union army utilized "Total War" tactics, burning cities like Atlanta to the ground and destroying the entire civilian infrastructure of the South.
    """)


# --- TAB 4: MACRO CASUALTY ANALYTICS ---
with tab4:
    st.header("Macro Casualty Analytics Across Centuries")
    st.markdown("A quantitative breakdown of human life lost across major global conflicts, emphasizing the disproportionate impact on civilian populations.")
    
    st.dataframe(
        df_historical.style.format({
            "Military Casualties": "{:,}", 
            "Civilian Casualties": "{:,}", 
            "Total Casualties": "{:,}"
        }), 
        use_container_width=True
    )
    
    st.subheader("Civilian vs. Military Casualties Comparison")
    chart_data = df_historical.set_index("War").sort_values("Total Casualties", ascending=True)[["Military Casualties", "Civilian Casualties"]]
    st.bar_chart(chart_data, height=550)

# Footer
st.markdown("---")
st.caption("Data sources: Historical records, ACLED, geopolitical trackers. Note: Casualty figures are estimates based on historical consensus. The realities of war depicted here are based on factual historical accounts to preserve the memory of those impacted.")