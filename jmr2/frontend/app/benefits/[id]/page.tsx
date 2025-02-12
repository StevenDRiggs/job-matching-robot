export default async function Benefit({
  params,
}: {
  params: Promise<{ id: number }>
}) {
  const id = (await params).id
  return <h2>Benefit {id}</h2>
}
