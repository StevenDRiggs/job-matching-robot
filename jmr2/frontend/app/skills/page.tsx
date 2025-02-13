import Link from 'next/link'

require('@dotenvx/dotenvx').config()


export default async function SkillsIndex() {
  const skills = await fetch(`${process.env.BACKEND}/skills`)
  .then((data) => data.json())
  .then((json) => JSON.parse(json))

  return (
    <>
      <h2>Skills Index</h2>
      <ul>
        {skills.map((skill) => (
          <Link href="/skills/{skill.tag}">
            <li key={skill.pk}>{skill.fields.tag}</li>
          </Link>
        ))}
      </ul>
    </>
  )
}
