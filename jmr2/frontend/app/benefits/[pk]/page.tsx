require('@dotenvx/dotenvx').config()


export default async function Benefit({
  params,
}: {
  params: Promise<{ pk: number }>
}) {
  const { pk } = await params
  const benefit = await fetch(`${process.env.BACKEND}/benefits/${pk}`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))

  return (
    <>
      <h3>{benefit.tag}</h3>
      <p>{benefit.description}</p>
    </>
  )
}
