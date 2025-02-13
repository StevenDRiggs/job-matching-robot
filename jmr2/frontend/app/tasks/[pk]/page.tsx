require('@dotenvx/dotenvx').config()


export default async function Task({
  params,
}: {
  params: Promise<{ pk: number }>
}) {
  const { pk } = await params
  const task = await fetch(`${process.env.BACKEND}/tasks/${pk}`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))
  .then((task_as_arr) => task_as_arr[0])

  return (
    <>
      <h3>{task.fields.tag}</h3>
    </>
  )
}
