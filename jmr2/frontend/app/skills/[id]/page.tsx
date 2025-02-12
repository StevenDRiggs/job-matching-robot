export default async function Skill({
  params,
}: {
  params: Promise<{ id: number }>
}) {
  const id = (await params).id
  return <h2>Skill {id}</h2>
}
