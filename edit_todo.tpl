<form action="/todo/{{task_id}}" method='POST'>
    <input type="hidden" name="_method" value="PATCH" />
    <label for="task">Update task:</label>
    <input type="text" name="task" value="{{task}}" required>
    <button type="submit">Update Task</button>
</form>