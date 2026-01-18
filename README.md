# realms-of-pythonia-record-system

Python OOP practice project extending the original realms-of-pythonia world with classes, objects, inheritance, and basic combat mechanics in a fantasy realm setting.

## Project overview

This continuation project rebuilds the realms of Pythonia using an **object**‑oriented design centred around creatures, realms, and a battle arena. 
Players can explore realms, inspect and buff fairy creatures, add quests, and start battles between named creatures through a simple console menu system. 

## What this project demonstrates

This project was created to practise core Python OOP concepts beyond the original dictionaries-and-JSON implementation. 
Key skills demonstrated include defining classes with attributes and methods, using inheritance and composition, and coordinating multiple objects through a menu‑driven main program. 

- Defining and instantiating classes such as `Creature`, `FairyCreature`, `Realm`, `RealmsRegistry`, and `BattleArena`. 
- Using inheritance to extend creature behaviour, for example having `FairyCreature` inherit from `Creature` and add special fairy-only actions. 
- Encapsulating realm data and lookups inside `Realm` and `RealmsRegistry` instead of relying on nested dictionaries.  
- Implementing interactions between objects, such as creatures battling each other and taking damage inside the `BattleArena`.

## Main features

- Creature system: Each creature has a name, type, health value, and a list of quests, with methods to add quests, attack, take damage, heal, and list quest status. 
- Fairy specialisation: `FairyCreature` can receive a “fairy dust” boost that increases health and prints a themed status message. 
- Realm management: `Realm` objects track creatures in that realm, while `RealmsRegistry` sets up the initial realms (such as Crimson Mountains and Whispering Woods) and provides search utilities.  
- Battle arena: `BattleArena` runs a turn‑based fight loop where two creatures attack until one is defeated, then heals both combatants afterwards.  
- Menu‑driven interface: A text menu lets the user display all realms and creatures, find and buff a creature, add quests to fairies, start a battle, or exit the program. 

