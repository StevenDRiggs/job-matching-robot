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
  .then((position_as_arr) => position_as_arr[0])

  return (
    <>
      <h3>{position.fields.title}</h3>
      <table>
        <tbody>
          {Object.keys(position.fields).map((field) => (
            <tr key={field}>
              <td>{field}</td>
              <td>{JSON.stringify(position.fields[field])}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  )
}
