| Feature        | Tuple `()`        | List `[]`         | Set `{}` or `set()` | Dictionary `{k:v}` |
|----------------|-------------------|-------------------|---------------------|--------------------|
| **Mutability** | Immutable         | Mutable           | Mutable             | Mutable            |
| **Ordering**   | Ordered           | Ordered           | Unordered           | Unordered |
| **Uniqueness** | Duplicates allowed| Duplicates allowed| **Unique** elements | **Unique Keys**    |
| **Access**     | Index             | Index             | No Index (Membership)| Key                |
| **Syntax**     | `(1, 2)`          | `[1, 2]`          | `{1, 2}` / `set()`  | `{'a': 1, 'b': 2}` |
| **Use When**   | Fixed collection, dict keys | Flexible collection, sequence | Uniqueness needed, set math | Key-value lookup, structured data |
