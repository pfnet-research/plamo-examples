const { OpenAI } = require('openai')

const openai = new OpenAI({
  baseURL: 'https://platform.preferredai.jp/api/completion/v1',
  apiKey: process.env.PLAMO_API_KEY
  // other params...
});

async function main() {
    const response = await openai.chat.completions.create({
    model: 'plamo-1.0-prime',
    messages: [
        {role: 'system', content:'あなたは学校の先生です'},
        { role: 'user', content: '二次方程式の解の公式を端的に教えてください' }
    ],
    });
    console.log(response.choices[0].message);
}

main();