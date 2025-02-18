require('@dotenvx/dotenvx').config()


export default async function Trait({
  params,
}: {
  params: Promise<{ pk: number }>
}) {
  const { pk } = await params
  const trait = await fetch(`${process.env.BACKEND}/traits/${pk}`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))

  return (
    <>
      <h3>{trait.tag}</h3>
    </>
  )
}
