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
  .then((benefit_as_arr) => benefit_as_arr[0])

  return (
    <>
      <h3>{benefit.fields.tag}</h3>
      <p>{benefit.fields.description}</p>
    </>
  )
}
