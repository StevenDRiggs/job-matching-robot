export default async function Trait({
  params,
}: {
  params: Promise<{ id: number }>
}) {
  const id = (await params).id
  return <h2>Trait {id}</h2>
}
