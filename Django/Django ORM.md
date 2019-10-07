# Django ORM

## Read

```python
questions.object.get(id=)
```

- 있는 데이터만 가져올수있다.
- 해당 데이터가 없을 경우 에러





## 1:N

- Qusetion : Answer => 1 : N > `answer_set`

  ```
  In [11]: question.answer_set.all()
  Out[11]: <QuerySet [<Answer: Answer object (1)>, <Answer: Answer object (2)>]>
  ```

  - `question.answer` 로는 가져올 수 없다.
  - 항상 복수라고 생각

- Answer : Question => N : 1 > `question`

  ```
  In [12]: answer.question
  Out[12]: <Question: Question object (1)>
  ```

  