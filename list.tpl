<h1>Hello welcome to organised todos... </h1>
<table border=1px solid >
    <tr>
        <th>Task</th>
        <th>Status</th>
    </tr>
    %for task in tasks:
    <tr>
        <td>{{task[1]}}</td>
        <td>
            <input type="checkbox" name="status" value="{{task[0]}}" {%if task[2]%}checked {%endif%} >
        </td>
    </tr>
    %end

</table>
<br>
#not working figure out a solution
# <button> <a href={add_todo.tpl}>Add a task</a></button>
