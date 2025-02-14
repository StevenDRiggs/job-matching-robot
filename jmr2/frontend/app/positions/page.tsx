import Link from 'next/link'

require('@dotenvx/dotenvx').config()


export default async function PositionsIndex() {
  const positions = await fetch(`${process.env.BACKEND}/positions`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))

  return (
    <>
      <h2>Positions Index</h2>
      <ul>
        {positions.map((position) => (
          <Link href={`/positions/${position.pk}`} key={position.pk}>
            <li>{position.title}</li>
          </Link>
        ))}
      </ul>
    </>
  )
}
