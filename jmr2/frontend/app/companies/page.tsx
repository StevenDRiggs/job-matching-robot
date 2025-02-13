require('@dotenvx/dotenvx').config()


export default async function CompaniesIndex() {
  console.log(`${process.env.BACKEND}/companies`)
  const companies = await fetch(`${process.env.BACKEND}/companies`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))
  console.log(companies)

  return (
    <>
      <h2>Companies Index</h2>
      <ul>
        {companies.map((company) => (
          <li key={company.pk}>{company.fields.name}</li>
        ))}
      </ul>
    </>
  )
}
