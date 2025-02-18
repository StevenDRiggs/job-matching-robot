require('@dotenvx/dotenvx').config()

import Link from 'next/link'


export default async function Position({
  params,
}: {
  params: Promise<{ pk: number }>
}) {
  const { pk } = await params
  const position = await fetch(`${process.env.BACKEND}/positions/${pk}`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))

  const subrender = (classType: String, requirementLevel: String) => {
    if (position[classType][requirementLevel].length <= 0) {
      return ''
    } else {
      return (
        <>
          <tr>
            <td><em>{requirementLevel.charAt(0).toUpperCase() + requirementLevel.substring(1).toLowerCase()}</em></td>
            <td></td>
          </tr>
          <tr>
            <td></td>
            <td>
              <table>
                <tbody>
                  {position[classType][requirementLevel].map(({ pk, tag, level }) => (
                    <tr key={pk}>
                      <td><Link href={`/${classType}/${pk}`}>{tag}</Link></td>
                      <td> level </td>
                      <td>{level}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </td>
          </tr>
        </>
      )
    }
  }

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
                  {position.benefits.map(({ pk, tag, available }) => (
                    <tr key={pk}>
                      <td><Link href={`/benefits/${pk}`}>{tag}</Link></td>
                      <td><em>{available}</em></td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </td>
          </tr>
          <tr>
            <td><strong>Tasks</strong></td>
            <td>
              <ul>
                {position.tasks.map(({ pk, tag }) => (
                  <li key={pk}><Link href={`/tasks/${pk}`}>{tag}</Link></li>
                ))}
              </ul>
            </td>
          </tr>
          <tr>
            <td><strong>Skills</strong></td>
            <td>
              <table>
                <tbody>
                  {subrender('skills', 'required')}
                  {subrender('skills', 'preferred')}
                  {subrender('skills', 'bonus')}
                </tbody>
              </table>
            </td>
          </tr>
          <tr>
            <td><strong>Traits</strong></td>
            <td>
              <table>
                <tbody>
                  {subrender('traits', 'required')}
                  {subrender('traits', 'preferred')}
                  {subrender('traits', 'bonus')}
                </tbody>
              </table>
            </td>
          </tr>
        </tbody>
      </table>
    </>
  )
}
