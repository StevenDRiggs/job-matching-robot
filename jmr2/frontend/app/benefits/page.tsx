require('@dotenvx/dotenvx').config()


export default async function BenefitsIndex() {
  const benefits = await fetch(`${process.env.BACKEND}/benefits`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))

  return (
    <>
      <h2>Benefits Index</h2>
      <ul>
        {benefits.map((benefit) => (
          <li key={benefit.pk}>{benefit.fields.name}</li>
        ))}
      </ul>
    </>
  )
}
