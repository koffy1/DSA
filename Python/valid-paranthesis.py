class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2 or len(s) % 2 != 0:
            return False
        
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        
        close = {'(' : ')', '[' : ']', '{' : '}'}
        checked = []
        calc = 0
        for i in s:
            if i == '(' or i == '{' or i == '[':
                checked.append(i)
                calc += 1
            else:
                if len(checked) == 0:
                    return False
                
                lastChecked = checked[-1]
                if close[lastChecked] == i:
                    calc -= 1
                    checked.pop()
                else:
                    return False
        if len(checked) == 0 and calc == 0:
            return True
        return False
                
        