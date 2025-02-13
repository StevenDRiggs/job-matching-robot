require('@dotenvx/dotenvx').config()


export default async function Skill({
  params,
}: {
  params: Promise<{ pk: number }>
}) {
  const { pk } = await params
  const skill = await fetch(`${process.env.BACKEND}/skills/${pk}`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))
  .then((skill_as_arr) => skill_as_arr[0])

  return (
    <>
      <h3>{skill.fields.tag}</h3>
    </>
  )
}
