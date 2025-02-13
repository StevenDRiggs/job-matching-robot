import Link from 'next/link'

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
          <Link href={`/tasks/${task.pk}`} key={task.pk}>
            <li>{task.fields.tag}</li>
          </Link>
        ))}
      </ul>
    </>
  )
}
