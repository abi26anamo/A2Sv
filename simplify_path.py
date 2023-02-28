class Solution:
    def simplifyPath(self, path: str) -> str:
        list_path = path.split("/")
        stack = []
        for path in list_path:
            if path== "" or path == '.':
                continue
            elif stack and path=="..":
                stack.pop()
            elif not stack and path=="..":
                continue
            else:
                stack.append(path)
        
        return "/" + "/".join(stack)
