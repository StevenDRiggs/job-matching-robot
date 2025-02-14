require('@dotenvx/dotenvx').config()


export default async function Position({
  params,
}: {
  params: Promise<{ pk: number }>
}) {
  const { pk } = await params
  const position = await fetch(`${process.env.BACKEND}/positions/${pk}`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))

  return (
    <>
      <h3>{position.title}</h3>
      <table>
        <tbody>
          <tr>
            <td><strong>Company</strong></td>
            <td>{position.company}</td>
          </tr>
          <tr>
            <td><strong>Description</strong></td>
            <td>{position.description}</td>
          </tr>
          <tr>
            <td><strong>Location</strong></td>
            <td>{position.location}</td>
          </tr>
          <tr>
            <td><strong>Relocation Assistance</strong></td>
            <td>{position.relocation_assistance}</td>
          </tr>
          <tr>
            <td><strong>Position Type</strong></td>
            <td>{position.position_type}</td>
          </tr>
          <tr>
            <td><strong>Pay</strong></td>
            <td>{position.pay.amount} {position.pay.currency} {position.pay.frequency}</td>
          </tr>
          <tr>
            <td><strong>Hours</strong></td>
            <td>{position.hours}</td>
          </tr>
          <tr>
            <td><strong>Benefits</strong></td>
            <td>
              <table>
                <tbody>

                </tbody>
              </table>
            </td>
          </tr>
          {Object.keys(position).map((field) => (
            <tr key={field}>
              <td>{field}</td>
              <td>{JSON.stringify(position[field])}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  )
}
