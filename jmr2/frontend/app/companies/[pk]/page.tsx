require('@dotenvx/dotenvx').config()


export default async function Company({
  params,
}: {
  params: Promise<{ pk: number }>
}) {
  const { pk } = await params
  const company = await fetch(`${process.env.BACKEND}/companies/${pk}`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))
  .then((company_as_arr) => company_as_arr[0])

  return (
    <>
      <h3>{company.fields.name}</h3>
    </>
  )
}
