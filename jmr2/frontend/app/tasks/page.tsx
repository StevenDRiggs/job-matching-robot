require('@dotenvx/dotenvx').config()


export default async function TasksIndex() {
  const tasks = await fetch(`${process.env.BACKEND}/tasks`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))

  return (
    <>
      <h2>Tasks Index</h2>
      <ul>
        {tasks.map((task) => (
          <li key={task.pk}>{task.fields.tag}</li>
        ))}
      </ul>
    </>
  )
}
