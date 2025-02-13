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
  .then((trait_as_arr) => trait_as_arr[0])

  return (
    <>
      <h3>{trait.fields.tag}</h3>
    </>
  )
}
