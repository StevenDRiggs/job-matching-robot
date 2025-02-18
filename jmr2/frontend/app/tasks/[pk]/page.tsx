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

  return (
    <>
      <h3>{task.tag}</h3>
    </>
  )
}
