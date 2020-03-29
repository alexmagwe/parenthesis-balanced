from stack import Stack
import time
p='{}{{{}}{{{{}}}}}'
s=Stack()
for item in p:
    if item=="{" :
        if s.peek()!=item and  not s.is_empty():
            s.pop()
        elif s.peek()==item or s.is_empty():
            s.push(item)
    
        print(s.stack())
    elif item=="}":
        if s.is_empty() or s.peek()==item:
            s.push(item)
        
            print(s.stack())
            continue   
        elif s.peek()!=item:
            s.pop()
        
            print(s.stack())
print('final stack',s.stack())
print('parenthesis are balanced') if s.is_empty() else print('unbalanced parenthesis')
    