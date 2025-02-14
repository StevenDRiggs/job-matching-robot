import Link from 'next/link'

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
          <Link href={`/benefits/${benefit.pk}`} key={benefit.pk}>
            <li>{benefit.tag}</li>
          </Link>
        ))}
      </ul>
    </>
  )
}
