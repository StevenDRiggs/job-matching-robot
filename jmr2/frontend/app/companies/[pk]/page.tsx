import Link from 'next/link'

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

  return (
    <>
      <h3>{company.name}</h3>
      <h4>Positions:</h4>
      <ul>
        {company.positions.map(({ pk, title }) => (
          <li key={pk}>
            <Link href={`/positions/${pk}`}>{title}</Link>
          </li>
        ))}
      </ul>
    </>
  )
}
