export default async function Task({
  params,
}: {
  params: Promise<{ id: number }>
}) {
  const id = (await params).id
  return <h2>Task {id}</h2>
}
