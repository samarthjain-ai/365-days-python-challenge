actions = []

def perform_action(action):
    actions.append(action)
    print("Action performed:", action)

def undo_action():
    if len(actions) == 0:
        print("Nothing to undo")
    else:
        removed = actions.pop()
        print("Undo:", removed)

def show_actions():
    print("Current Actions:", actions)


perform_action("Write Hello")
perform_action("Add Python")
perform_action("Add AI")

show_actions()

undo_action()

show_actions()
