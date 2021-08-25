# Aika
Sublime Text plugin for calculating hours and minutes in work day.

## Installation
- Copy aika-directory to e.g. /Users/topipo/Library/ApplicationSupport/Sublime Text 3/Packages

```
cp -r aika "/Users/topipo/Library/ApplicationSupport/Sublime Text 3/Packages"
```

## Usage
- Start Sublime Text 3
- Select text with start and end times, e.g.

```
8:15
Task A
Task B
16:00
```

- Press alt+command+a
- Work day duration should appear below end time, e.g.

```
8:15
Task A
Task B
16:00

7:45
```

- See View -> Show Console if it does not work

## Key Binding

Add to Sublime Text -> Preferences -> Key Bindings:

```
    { "keys": ["alt+command+a"], "command": "aika" }

```
