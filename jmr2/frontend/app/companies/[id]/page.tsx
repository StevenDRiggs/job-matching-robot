export default async function Company({
  params,
}: {
  params: Promise<{ id: number }>
}) {
  const id = (await params).id
  return <h2>Company {id}</h2>
}
