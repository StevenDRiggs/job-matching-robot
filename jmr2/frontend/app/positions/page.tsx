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
          <li key={position.pk}>{position.fields.title}</li>
        ))}
      </ul>
    </>
  )
}
