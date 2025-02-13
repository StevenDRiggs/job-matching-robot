require('@dotenvx/dotenvx').config()


export default async function TraitsIndex() {
  const traits = await fetch(`${process.env.BACKEND}/traits`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))

  return (
    <>
      <h2>Traits Index</h2>
      <ul>
        {traits.map((trait) => (
          <li key={trait.pk}>{trait.fields.tag}</li>
        ))}
      </ul>
    </>
  )
}
