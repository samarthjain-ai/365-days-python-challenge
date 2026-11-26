actions = []

actions.append("Write Hello")
actions.append("Add Python")
actions.append("Add AI")

print("Before Undo:", actions)

actions.pop()

print("After Undo:", actions)