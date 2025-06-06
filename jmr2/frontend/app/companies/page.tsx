import Link from 'next/link'

require('@dotenvx/dotenvx').config()


export default async function CompaniesIndex() {
  const companies = await fetch(`${process.env.BACKEND}/companies`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))

  return (
    <>
      <h2>Companies Index</h2>
      <ul>
        {companies.map((company) => (
          <Link href={`/companies/${company.pk}`} key={company.pk}>
            <li>{company.name}</li>
          </Link>
        ))}
      </ul>
    </>
  )
}
