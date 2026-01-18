# realms-of-pythonia-record-system

Python OOP practice project extending the original realms-of-pythonia world with classes, objects, inheritance, and basic combat mechanics in a fantasy realm setting. [file:3]

## Project overview

This continuation project rebuilds the realms of Pythonia using an **object**‑oriented design centred around creatures, realms, and a battle arena. [file:3]  
Players can explore realms, inspect and buff fairy creatures, add quests, and start battles between named creatures through a simple console menu system. [file:3]

## What this project demonstrates

This project was created to practise core Python OOP concepts beyond the original dictionaries-and-JSON implementation. [file:3]  
Key skills demonstrated include defining classes with attributes and methods, using inheritance and composition, and coordinating multiple objects through a menu‑driven main program. [file:3]

- Defining and instantiating classes such as `Creature`, `FairyCreature`, `Realm`, `RealmsRegistry`, and `BattleArena`. [file:3]  
- Using inheritance to extend creature behaviour, for example having `FairyCreature` inherit from `Creature` and add special fairy-only actions. [file:3]  
- Encapsulating realm data and lookups inside `Realm` and `RealmsRegistry` instead of relying on nested dictionaries. [file:3]  
- Implementing interactions between objects, such as creatures battling each other and taking damage inside the `BattleArena`. [file:3]

## Main features

- Creature system: Each creature has a name, type, health value, and a list of quests, with methods to add quests, attack, take damage, heal, and list quest status. [file:3]  
- Fairy specialisation: `FairyCreature` can receive a “fairy dust” boost that increases health and prints a themed status message. [file:3]  
- Realm management: `Realm` objects track creatures in that realm, while `RealmsRegistry` sets up the initial realms (such as Crimson Mountains and Whispering Woods) and provides search utilities. [file:3]  
- Battle arena: `BattleArena` runs a turn‑based fight loop where two creatures attack until one is defeated, then heals both combatants afterwards. [file:3]  
- Menu‑driven interface: A text menu lets the user display all realms and creatures, find and buff a creature, add quests to fairies, start a battle, or exit the program. [file:3]

